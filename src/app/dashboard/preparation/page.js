'use client';
import { useState, useEffect } from 'react';

export default function PreparationPage() {
    const [activeTab, setActiveTab] = useState('Psychological Tests');
    const [loading, setLoading] = useState(false);
    const [results, setResults] = useState([]);
    const [promptData, setPromptData] = useState(null);

    // Tabs
    const tabs = [
        "Intelligence Test",
        "Psychological Tests",
        "GTO Tests",
        "Deputy President Interview",
        "Psychologist Interview"
    ];

    // Types of Psych tests
    const psychTypes = [
        { label: 'WAT (Word Association)', type: 'WAT', limit: 10 },
        { label: 'SCT (Sentence Completion)', type: 'SCT', limit: 5 },
        { label: 'Pointer Story', type: 'Story', limit: 3 },
        { label: 'Picture Story', type: 'Story', limit: 3, isPic: true },
        { label: 'Situation Reaction Test', type: 'SRT', limit: 3 }
    ];

    const [activePsych, setActivePsych] = useState(psychTypes[0]);
    const [dbData, setDbData] = useState(null);

    // For picture stories
    const randomPics = ['pic1.jpg', 'pic2.jpg', 'pic3.jpg', 'pic4.jpg', 'pic5.jpg'];
    const [currentPic, setCurrentPic] = useState('');

    // Fetch local DB mapping once
    useEffect(() => {
        fetch('/data/data.json')
            .then(res => res.json())
            .then(data => setDbData(data))
            .catch(err => console.error("Error loading mock data", err));
    }, []);

    const handleGenerate = async () => {
        if (!dbData) return;
        setLoading(true);
        setResults([]);

        let inputStr = "";

        if (activePsych.type === 'WAT') {
            const wats = dbData.wat;
            inputStr = wats[Math.floor(Math.random() * wats.length)];
        } else if (activePsych.type === 'SCT') {
            const scts = dbData.sct_english;
            inputStr = scts[Math.floor(Math.random() * scts.length)];
        } else if (activePsych.type === 'Story' && !activePsych.isPic) {
            const pointers = dbData.pointer_stories;
            inputStr = pointers[Math.floor(Math.random() * pointers.length)];
        } else if (activePsych.isPic) {
            inputStr = "Write a story based on the picture shown. The main character is 29 years old.";
            setCurrentPic(`/images/${randomPics[Math.floor(Math.random() * randomPics.length)]}`);
        } else if (activePsych.type === 'SRT') {
            const srts = dbData.srt;
            inputStr = srts[Math.floor(Math.random() * srts.length)];
        }

        setPromptData(inputStr);

        try {
            const res = await fetch('/api/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    type: activePsych.type,
                    inputs: inputStr,
                    variations: activePsych.limit
                })
            });
            const resData = await res.json();
            if (resData.results) {
                setResults(resData.results);
            } else {
                setResults(['Error generating responses. Check API key.']);
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

            {activeTab === 'Psychological Tests' ? (
                <div style={{ display: 'flex', gap: '2rem' }}>
                    {/* Sub menu for Psych Tests */}
                    <div style={{ width: '250px', display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
                        {psychTypes.map(pt => (
                            <button
                                key={pt.label}
                                onClick={() => { setActivePsych(pt); setResults([]); setPromptData(null); }}
                                className="btn-secondary"
                                style={{
                                    textAlign: 'left',
                                    background: activePsych.label === pt.label ? 'rgba(59, 130, 246, 0.2)' : 'transparent',
                                    border: 'none',
                                    borderLeft: activePsych.label === pt.label ? '3px solid var(--accent-color)' : '3px solid transparent',
                                    borderRadius: '0 8px 8px 0'
                                }}
                            >
                                {pt.label}
                            </button>
                        ))}
                    </div>

                    {/* Interactive Workspace */}
                    <div className="glass-panel" style={{ flex: '1' }}>
                        <h2>{activePsych.label} Practice</h2>
                        <p style={{ marginBottom: '1.5rem' }}>
                            Click below to draw a random prompt and generate <strong>{activePsych.limit} AI variations</strong> tailored for a 29-year-old leader.
                        </p>

                        <button className="btn-primary" onClick={handleGenerate} disabled={loading || !dbData}>
                            {loading ? 'AI is Thinking...' : 'Generate New Prompt & Answers'}
                        </button>

                        {promptData && (
                            <div style={{ marginTop: '2rem', padding: '1.5rem', background: 'rgba(0,0,0,0.3)', borderRadius: '8px', border: '1px solid var(--glass-border)' }}>
                                <h3 style={{ color: '#c084fc', marginBottom: '1rem' }}>Prompt:</h3>

                                {activePsych.isPic && currentPic && (
                                    <img src={currentPic} alt="ISSB Picture Story" style={{ width: '100%', maxWidth: '400px', borderRadius: '8px', marginBottom: '1rem' }} />
                                )}

                                <p style={{ fontSize: '1.25rem', fontWeight: '500', color: 'white' }}>{promptData}</p>

                                <div style={{ marginTop: '2rem' }}>
                                    <h4 style={{ color: '#10b981', marginBottom: '1rem' }}>AI Variations ({results.length}):</h4>
                                    {loading ? (
                                        <div className="fade-in">Loading variations mapping to 14 OLQs...</div>
                                    ) : (
                                        <ul style={{ listStylePosition: 'inside', display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                                            {results.map((res, i) => (
                                                <li key={i} className="fade-in" style={{ padding: '1rem', background: 'rgba(255,255,255,0.05)', borderRadius: '8px', borderLeft: '3px solid #3b82f6' }}>
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
            ) : (
                <div className="glass-panel text-center">
                    <h2 style={{ color: 'var(--text-secondary)' }}>{activeTab} module is under construction...</h2>
                    <p>This module will be populated similarly based on the final curriculum.</p>
                </div>
            )}
        </div>
    );
}
