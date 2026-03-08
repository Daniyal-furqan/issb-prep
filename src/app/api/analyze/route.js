import { NextResponse } from 'next/server';
import { verifyToken } from '@/lib/auth';

const SYSTEM_PROMPT = `
You are an expert Military Psychologist selecting candidates for the Armed Forces (ISSB). 
The candidate is a 29-year-old male applying on the basis of a graduate course.

Your task is to analyze the candidate's self-reported "Merits", "Demerits", and "Unforgettable Accident".
Provide a psychological assessment of their personality based on these inputs. 
Evaluate if their answers are appropriate for an officer candidate, pointing out any red flags (like extreme negativity, lack of emotional stability, weak responsibility) and highlighting strong points (14 Officer Like Qualities).

Use VERY simple, direct English. Be constructive. 
Structure your response exactly like this:
1. **Psychological Profile**: (Brief overview of the traits projected)
2. **Analysis of Merits**: (Are they genuine? Do they show OLQs?)
3. **Analysis of Demerits**: (Are they acceptable human flaws or dangerous red flags?)
4. **Analysis of Accident**: (Does it show emotional trauma, or resilience and learning?)
5. **Final Verdict & Recommendations**: (How to improve these answers before the real test)
`;

export async function POST(req) {
    try {
        const authCookie = req.cookies.get('auth_token')?.value;
        if (!authCookie) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });

        const tokenData = verifyToken(authCookie);
        if (!tokenData) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });

        const { merits, demerits, accident } = await req.json();

        const userPrompt = `
    Candidate's Merits: "${merits}"
    Candidate's Demerits: "${demerits}"
    Unforgettable Accident: "${accident}"
    
    Please analyze this profile.
    `;

        const res = await fetch('https://api.openai.com/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`
            },
            body: JSON.stringify({
                model: 'gpt-4o', // using 4o for better analysis
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

        const responseText = aiData.choices[0].message.content.trim();

        return NextResponse.json({ analysis: responseText });

    } catch (error) {
        console.error('API Analyze Error', error);
        return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
    }
}
