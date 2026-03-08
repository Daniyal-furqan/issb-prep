import { NextResponse } from 'next/server';
import { verifyToken } from '@/lib/auth';

const SYSTEM_PROMPT = `
You are an expert Psychologist and a Leader designed to help a 29-year-old candidate prepare for the ISSB (Inter Services Selection Board) Armed Forces selection.

**Your Persona & Constraints:**
- You are acting for a 29-year-old male candidate.
- You must use VERY simple, natural, everyday English. Short sentences (7-8 seconds to write, so max 3 to 6 words generally, unless it's a story).
- NO negativity. Avoid words like 'die', 'loss', 'accident', 'fail' unless strictly required by the prompt, but counter them with extreme positivity.
- Every response must subtly reflect the 14 Officer Like Qualities (OLQs) (Planning, Responsibility, Emotional Stability, Courage, Integrity, Determination, Social Relations, Initiative, Practical Ability, Influencing Ability, General Awareness, Expressions, Physical Endurance, Self Confidence) without explicitly naming them (e.g., Don't say "I am a responsible person").
- If writing a story, include ONE main character, overcome a challenge positively, and end with success/happiness. Story must be written in 3.5 minutes (about 80-100 words).
- If answering SRTs (Situation Reaction Tests), be exact, precise, and practical. Priorities: 1. Duty, 2. Family, 3. Others. Be emotionally stable. Explain the exact action you will take without assumptions.

**Task Rules:**
- For WAT (Word Association Test): The user will provide a word. You must return EXACTLY the requested number of variations (default 10) of short, positive sentences (max 4-5 words) using the word.
- For SCT (Sentence Completion): The user will provide a starting phrase. You must return EXACTLY the requested number of variations (default 5). Complete the sentence positively and shortly.
- For Pointer/Picture Story: The user will provide a starter. Return the requested number of variations (default 3) of short stories (80-100 words each). End with success.

Return the response as a clear, formatted JSON ARRAY of strings, like this:
["variation 1", "variation 2", "variation 3"]
Do NOT include extra text or markdown formatting outside the JSON array. Just the JSON array.
`;

export async function POST(req) {
    try {
        const authCookie = req.cookies.get('auth_token')?.value;
        if (!authCookie) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });

        // Verify token to ensure security
        const tokenData = verifyToken(authCookie);
        if (!tokenData) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });

        const { type, inputs, variations } = await req.json();

        let userPrompt = "";
        if (type === "WAT") {
            userPrompt = `Word: "${inputs}". Generate ${variations} variations of a short, positive sentence (max 5 words) using this word.`;
        } else if (type === "SCT" || type === "SCT_Urdu") {
            userPrompt = `Starter: "${inputs}". Generate ${variations} variations to complete this sentence positively and shortly. If the starter was in Urdu, feel free to reply in Roman Urdu or English.`;
        } else if (type === "Essay") {
            userPrompt = `Topic: "${inputs}". Generate ${variations} different highly structured, 150-word ISSB essay outlines/points (Intro, body, conclusion) emphasizing leadership.`;
        } else if (type === "Story") {
            userPrompt = `Starter: "${inputs}". Generate ${variations} variations of a story (80 words max) featuring a 29-year-old main character who overcomes a challenge and achieves success.`;
        } else if (type === "SRT") {
            userPrompt = `Situation: "${inputs}". Generate ${variations} variations of exact, practical actions prioritizing Duty > Family > Others, without assumptions.`;
        } else if (type === "Verbal" || type === "NonVerbal") {
            userPrompt = `Target: "${type} Intelligence Test". Generate ${variations} challenging ISSB intelligence multiple-choice questions with answers based on the target type. Keep the format concise.`;
        } else if (type.startsWith("GTO")) {
            userPrompt = `Target: "${type.replace("GTO_", "")} Test". Generate ${variations} distinct realistic scenarios or topics that a GTO would assign in ISSB. Include a sentence on what OLQs they test.`;
        } else if (type.includes("Interview")) {
            userPrompt = `Target: "${type.replace("_", " ")}". Generate ${variations} common, tough interview questions asked at ISSB, followed by a tip on how a leader should answer them.`;
        } else {
            userPrompt = `Prompt: "${inputs}". Generate ${variations} variations according to the persona.`;
        }

        const res = await fetch('https://api.openai.com/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`
            },
            body: JSON.stringify({
                model: 'gpt-4o-mini',
                messages: [
                    { role: 'system', content: SYSTEM_PROMPT },
                    { role: 'user', content: userPrompt }
                ],
                temperature: 0.7
            })
        });

        const aiData = await res.json();

        if (aiData.error) {
            console.error(aiData.error);
            return NextResponse.json({ error: aiData.error.message }, { status: 500 });
        }

        let responseText = aiData.choices[0].message.content.trim();

        // Attempt to parse JSON
        let results = [];
        try {
            if (responseText.startsWith('```json')) {
                responseText = responseText.replace(/```json/g, '').replace(/```/g, '');
            }
            results = JSON.parse(responseText);
        } catch (e) {
            // Fallback: split by newlines if array parsing fails
            results = responseText.split('\n').map(line => line.replace(/^-\s*/, '').trim()).filter(Boolean);
        }

        return NextResponse.json({ results });

    } catch (error) {
        console.error('API Gen Error', error);
        return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
    }
}
