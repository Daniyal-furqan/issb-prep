export default function DashboardHome() {
    return (
        <div>
            <h1 style={{ marginBottom: '1rem' }}>Dashboard Overview</h1>
            <p style={{ maxWidth: '800px', fontSize: '1.125rem' }}>
                Welcome to your ISSB Preparation Dashboard. To begin, select a module from the sidebar.
                Your journey begins with <strong>Introduction</strong>, moves to <strong>Preparation</strong>, and culminates with the <strong>Online Test</strong>.
            </p>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '2rem', marginTop: '3rem' }}>

                <div className="glass-panel">
                    <h3 style={{ color: 'var(--accent-color)' }}>Introduction</h3>
                    <p style={{ marginBottom: '1rem' }}>
                        Get familiar with the detailed 4-day testing schedule of ISSB. Understand what happens on Arrival Day up to Departure.
                    </p>
                    <a href="/dashboard/introduction" className="btn-secondary" style={{ display: 'inline-block', fontSize: '0.875rem' }}>View Schedule</a>
                </div>

                <div className="glass-panel">
                    <h3 style={{ color: '#c084fc' }}>Preparation</h3>
                    <p style={{ marginBottom: '1rem' }}>
                        Practice Word Association Tests (WAT), Sentence Completion, Pointer Stories, and more with our AI Psychologist guidance.
                    </p>
                    <a href="/dashboard/preparation" className="btn-secondary" style={{ display: 'inline-block', fontSize: '0.875rem' }}>Start Prep</a>
                </div>

                <div className="glass-panel">
                    <h3 style={{ color: '#10b981' }}>Online Test</h3>
                    <p style={{ marginBottom: '1rem' }}>
                        Take a simulated ISSB examination. Receive dynamic AI assessment to judge your 14 Officer Like Qualities (OLQs).
                    </p>
                    <a href="/dashboard/test" className="btn-secondary" style={{ display: 'inline-block', fontSize: '0.875rem' }}>Take Test</a>
                </div>

            </div>
        </div>
    );
}
