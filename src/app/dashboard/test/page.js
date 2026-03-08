'use client';
import { useState } from 'react';

export default function OnlineTestPage() {
    const [merits, setMerits] = useState('');
    const [demerits, setDemerits] = useState('');
    const [accident, setAccident] = useState('');

    const [loading, setLoading] = useState(false);
    const [analysis, setAnalysis] = useState('');
    const [error, setError] = useState('');

    const handleAnalyze = async (e) => {
        e.preventDefault();
        if (!merits || !demerits || !accident) {
            setError('Please fill in all fields before analyzing.');
            return;
        }

        setLoading(true);
        setError('');
        setAnalysis('');

        try {
            const res = await fetch('/api/analyze', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ merits, demerits, accident })
            });
            const data = await res.json();

            if (res.ok && data.analysis) {
                setAnalysis(data.analysis);
            } else {
                setError(data.error || 'Failed to fetch analysis.');
            }
        } catch (err) {
            setError('An error occurred while connecting to the AI.');
        }
        setLoading(false);
    };

    return (
        <div style={{ maxWidth: '900px', margin: '0 auto' }}>
            <h1 style={{ color: 'var(--accent-color)', marginBottom: '1rem' }}>Psychological Profiling Test</h1>
            <p style={{ marginBottom: '2rem', fontSize: '1.125rem' }}>
                The Military Psychologist assesses your personality through standardized questions.
                Input your Merits, Demerits, and an Unforgettable Accident below. The AI Psychologist will evaluate how well your answers reflect the 14 Officer Like Qualities.
            </p>

            {error && <div className="alert alert-error">{error}</div>}

            <div style={{ display: 'flex', gap: '2rem', alignItems: 'flex-start', flexWrap: 'wrap' }}>
                <form onSubmit={handleAnalyze} className="glass-panel" style={{ flex: '1', minWidth: '350px' }}>

                    <div className="input-group">
                        <label className="input-label" style={{ color: '#10b981', fontWeight: 'bold' }}>Your Merits (3 to 5 strong points)</label>
                        <textarea
                            className="input-field"
                            rows="4"
                            placeholder="e.g. 1. I take responsibility easily. 2. I am physically resilient..."
                            value={merits}
                            onChange={(e) => setMerits(e.target.value)}
                            required
                        ></textarea>
                    </div>

                    <div className="input-group">
                        <label className="input-label" style={{ color: '#ef4444', fontWeight: 'bold' }}>Your Demerits (3 to 5 weak points)</label>
                        <textarea
                            className="input-field"
                            rows="4"
                            placeholder="e.g. 1. I am sometimes blunt. 2. I trust people too quickly..."
                            value={demerits}
                            onChange={(e) => setDemerits(e.target.value)}
                            required
                        ></textarea>
                    </div>

                    <div className="input-group">
                        <label className="input-label" style={{ color: '#f59e0b', fontWeight: 'bold' }}>Unforgettable Accident (Brief description)</label>
                        <textarea
                            className="input-field"
                            rows="4"
                            placeholder="Briefly describe an unforgettable event and how you handled it..."
                            value={accident}
                            onChange={(e) => setAccident(e.target.value)}
                            required
                        ></textarea>
                    </div>

                    <button type="submit" className="btn-primary" style={{ width: '100%', marginTop: '1rem' }} disabled={loading}>
                        {loading ? 'Analyzing Profile...' : 'Submit to AI Psychologist'}
                    </button>
                </form>

                {(loading || analysis) && (
                    <div className="glass-panel fade-in" style={{ flex: '1', minWidth: '350px', borderTop: '4px solid #c084fc' }}>
                        <h2 style={{ color: '#c084fc', marginBottom: '1.5rem' }}>AI Assessor Report</h2>

                        {loading ? (
                            <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem', opacity: 0.7 }}>
                                <div style={{ height: '20px', background: 'rgba(255,255,255,0.1)', borderRadius: '4px', width: '100%' }}></div>
                                <div style={{ height: '20px', background: 'rgba(255,255,255,0.1)', borderRadius: '4px', width: '80%' }}></div>
                                <div style={{ height: '20px', background: 'rgba(255,255,255,0.1)', borderRadius: '4px', width: '90%' }}></div>
                                <div style={{ height: '20px', background: 'rgba(255,255,255,0.1)', borderRadius: '4px', width: '60%' }}></div>
                            </div>
                        ) : (
                            <div style={{ lineHeight: '1.8', color: 'var(--text-primary)' }}>
                                {analysis.split('\n').map((line, i) => {
                                    if (line.startsWith('1.') || line.startsWith('2.') || line.startsWith('3.') || line.startsWith('4.') || line.startsWith('5.')) {
                                        return <h3 key={i} style={{ marginTop: '1.5rem', marginBottom: '0.5rem', color: '#60a5fa' }}>{line.replace(/\*\*/g, '')}</h3>;
                                    } else if (line.trim() === '') {
                                        return <br key={i} />;
                                    }
                                    return <p key={i} style={{ marginBottom: '0.5rem' }}>{line.replace(/\*\*/g, '')}</p>;
                                })}
                            </div>
                        )}
                    </div>
                )}
            </div>
        </div>
    );
}
