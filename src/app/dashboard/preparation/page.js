'use client';
import { useState, useEffect } from 'react';

export default function PreparationPage() {
    const [activeTab, setActiveTab] = useState('Psychological Tests');
    const [loading, setLoading] = useState(false);
    const [results, setResults] = useState([]);
    const [promptData, setPromptData] = useState(null);
    const [dbData, setDbData] = useState(null);

    // Main Tabs
    const tabs = [
        "Psychological Tests",
        "Intelligence Test",
        "GTO Tests",
        "Interviews"
    ];

    // Subcategories for each tab
    const categories = {
        "Psychological Tests": [
            { label: 'Essays (English/Urdu)', type: 'Essay', limit: 3 },
            { label: 'WAT (Word Association)', type: 'WAT', limit: 10 },
            { label: 'SCT (Sentence Completion)', type: 'SCT', limit: 5 },
            { label: 'SCT (Urdu) Practice', type: 'SCT_Urdu', limit: 5 },
            { label: 'Pointer Story', type: 'Story', limit: 3 },
            { label: 'Picture Story', type: 'Story', limit: 3, isPic: true },
            { label: 'Situation Reaction Test', type: 'SRT', limit: 3 }
        ],
        "Intelligence Test": [
            { label: 'Verbal Intelligence', type: 'Verbal', limit: 5 },
            { label: 'Non-Verbal Intelligence', type: 'NonVerbal', limit: 5 }
        ],
        "GTO Tests": [
            { label: 'Group Discussion Topics', type: 'GTO_Discussion', limit: 3 },
            { label: 'Military Planning Ex (MPE)', type: 'GTO_Planning', limit: 2 },
            { label: 'Command Task Scenarios', type: 'GTO_Command', limit: 3 }
        ],
        "Interviews": [
            { label: 'Deputy President Interview', type: 'DP_Interview', limit: 5 },
            { label: 'Psychologist Interview', type: 'Psych_Interview', limit: 5 }
        ]
    };

    const [activeSub, setActiveSub] = useState(categories["Psychological Tests"][0]);

    // For picture stories
    const randomPics = ['pic1.jpg', 'pic2.jpg', 'pic3.jpg', 'pic4.jpg', 'pic5.jpg'];
    const [currentPic, setCurrentPic] = useState('');

    useEffect(() => {
        fetch('/data/data.json')
            .then(res => res.json())
            .then(data => setDbData(data))
            .catch(err => console.error("Error loading mock data", err));
    }, []);

    // When tab changes, reset sub selection
    useEffect(() => {
        setActiveSub(categories[activeTab][0]);
        setResults([]);
        setPromptData(null);
    }, [activeTab]);

    const handleGenerate = async () => {
        setLoading(true);
        setResults([]);
        let inputStr = "";

        // Determine input based on selection
        if (activeSub.type === 'WAT' && dbData?.wat) {
            inputStr = dbData.wat[Math.floor(Math.random() * dbData.wat.length)];
        } else if (activeSub.type === 'SCT' && dbData?.sct_english) {
            inputStr = dbData.sct_english[Math.floor(Math.random() * dbData.sct_english.length)];
        } else if (activeSub.type === 'SCT_Urdu' && dbData?.sct_urdu) {
            inputStr = dbData.sct_urdu[Math.floor(Math.random() * dbData.sct_urdu.length)];
        } else if (activeSub.type === 'Essay' && dbData?.essays) {
            inputStr = dbData.essays[Math.floor(Math.random() * dbData.essays.length)];
            inputStr = `Write a short ISSB essay on: "${inputStr}"`;
        } else if (activeSub.type === 'Story' && !activeSub.isPic && dbData?.pointer_stories) {
            inputStr = dbData.pointer_stories[Math.floor(Math.random() * dbData.pointer_stories.length)];
        } else if (activeSub.isPic) {
            inputStr = "Write a story based on a picture showing people in a discussion. The main character is 29 years old.";
            setCurrentPic(`/images/${randomPics[Math.floor(Math.random() * randomPics.length)]}`);
        } else if (activeSub.type === 'SRT' && dbData?.srt) {
            inputStr = dbData.srt[Math.floor(Math.random() * dbData.srt.length)];
        } else {
            // Generative AI fallback for GTO, Intelligence, Interviews since those weren't in the static JSON dump
            inputStr = `Generate a realistic ISSB ${activeSub.label} prompt/question for a 29-year old candidate. Provide the scenario clearly.`;
        }

        setPromptData(inputStr);

        try {
            const res = await fetch('/api/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    type: activeSub.type,
                    inputs: inputStr,
                    variations: activeSub.limit
                })
            });
            const resData = await res.json();
            if (resData.results) {
                setResults(resData.results);
            } else {
                setResults(['Error generating responses.']);
            }
        } catch (e) {
            setResults(['Fatal error generating results.']);
        }
        setLoading(false);
    };

    return (
        <div>
            <h1 style={{ color: 'var(--accent-color)', marginBottom: '1rem' }}>Preparation Module</h1>

            {/* Main Tabs */}
            <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap', marginBottom: '2rem', borderBottom: '1px solid var(--glass-border)', paddingBottom: '1rem' }}>
                {tabs.map(t => (
                    <button
                        key={t}
                        onClick={() => setActiveTab(t)}
                        className="btn-secondary"
                        style={{
                            background: activeTab === t ? 'var(--glass-bg)' : 'transparent',
                            borderColor: activeTab === t ? 'var(--accent-color)' : 'var(--glass-border)',
                            color: activeTab === t ? 'white' : 'var(--text-secondary)'
                        }}
                    >
                        {t}
                    </button>
                ))}
            </div>

            <div style={{ display: 'flex', gap: '2rem', flexWrap: 'wrap' }}>
                {/* Sub menu */}
                <div style={{ width: '280px', display: 'flex', flexDirection: 'column', gap: '0.5rem', flexShrink: 0 }}>
                    {categories[activeTab].map(sub => (
                        <button
                            key={sub.label}
                            onClick={() => { setActiveSub(sub); setResults([]); setPromptData(null); }}
                            className="btn-secondary"
                            style={{
                                textAlign: 'left',
                                background: activeSub.label === sub.label ? 'rgba(59, 130, 246, 0.2)' : 'transparent',
                                border: 'none',
                                borderLeft: activeSub.label === sub.label ? '3px solid var(--accent-color)' : '3px solid transparent',
                                borderRadius: '0 8px 8px 0'
                            }}
                        >
                            {sub.label}
                        </button>
                    ))}
                </div>

                {/* Interactive Workspace */}
                <div className="glass-panel" style={{ flex: '1', minWidth: '300px' }}>
                    <h2>{activeSub.label} Practice</h2>
                    <p style={{ marginBottom: '1.5rem', color: 'var(--text-secondary)' }}>
                        Click below to draw a prompt and generate <strong>{activeSub.limit} AI variations/examples</strong> tailored for leadership and 14 OLQs.
                    </p>

                    <button className="btn-primary" onClick={handleGenerate} disabled={loading || (!dbData && activeTab === 'Psychological Tests')}>
                        {loading ? 'AI is Thinking...' : 'Generate AI Session'}
                    </button>

                    {promptData && (
                        <div className="fade-in" style={{ marginTop: '2rem', padding: '1.5rem', background: 'rgba(0,0,0,0.3)', borderRadius: '8px', border: '1px solid var(--glass-border)' }}>
                            <h3 style={{ color: '#c084fc', marginBottom: '1rem' }}>Target Prompt:</h3>

                            {activeSub.isPic && currentPic && (
                                <img src={currentPic} alt="ISSB Picture Story" style={{ width: '100%', maxWidth: '400px', borderRadius: '8px', marginBottom: '1rem' }} />
                            )}

                            <p style={{ fontSize: '1.15rem', fontWeight: '500', color: 'white' }}>{promptData}</p>

                            <div style={{ marginTop: '2rem' }}>
                                <h4 style={{ color: '#10b981', marginBottom: '1rem' }}>AI Responses ({results.length}):</h4>
                                {loading ? (
                                    <div className="fade-in" style={{ color: 'var(--text-secondary)' }}>Generating high-quality psychological breakdown...</div>
                                ) : (
                                    <ul style={{ listStylePosition: 'inside', display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                                        {results.map((res, i) => (
                                            <li key={i} className="fade-in" style={{ padding: '1rem', background: 'rgba(255,255,255,0.05)', borderRadius: '8px', borderLeft: '3px solid #3b82f6', lineHeight: '1.6' }}>
                                                {res}
                                            </li>
                                        ))}
                                    </ul>
                                )}
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}
