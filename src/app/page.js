'use client';
import Link from 'next/link';

export default function Home() {
  return (
    <div className="container min-h-screen">
      <nav className="navbar fade-in">
        <div className="nav-brand">
          <span style={{ color: 'var(--accent-color)' }}>✦</span> ISSB Pro
        </div>
        <div style={{ display: 'flex', gap: '1rem' }}>
          <Link href="/login" className="btn-secondary">Log In</Link>
          <Link href="/signup" className="btn-primary">Sign Up</Link>
        </div>
      </nav>

      <main className="flex-center fade-in" style={{ minHeight: '70vh', flexDirection: 'column', textAlign: 'center' }}>
        <div className="glass-panel" style={{ maxWidth: '800px', padding: '4rem 2rem' }}>
          <h1>Master the ISSB like a Leader</h1>
          <p style={{ fontSize: '1.125rem', marginTop: '1.5rem', marginBottom: '2.5rem' }}>
            Experience an AI-powered psychologist that guides your preparation, evaluates your psychological tests, and refines your leadership qualities (OLQs).
          </p>

          <div style={{ display: 'flex', gap: '1rem', justifyContent: 'center' }}>
            <Link href="/signup" className="btn-primary" style={{ padding: '1rem 2.5rem', fontSize: '1.125rem' }}>
              Start Preparation
            </Link>
          </div>
        </div>

        <div style={{ display: 'flex', gap: '2rem', marginTop: '4rem', flexWrap: 'wrap', justifyContent: 'center' }}>
          <div className="glass-panel" style={{ flex: '1', minWidth: '250px' }}>
            <h3 style={{ color: '#60a5fa' }}>AI Psychologist</h3>
            <p>Get personalized feedback on your WAT, SCT, and Stories to ensure they reflect true leadership.</p>
          </div>
          <div className="glass-panel" style={{ flex: '1', minWidth: '250px' }}>
            <h3 style={{ color: '#c084fc' }}>Comprehensive Curriculum</h3>
            <p>Structured day-by-day guides from Arrival Day to Departure, fully equipped with practice tests.</p>
          </div>
          <div className="glass-panel" style={{ flex: '1', minWidth: '250px' }}>
            <h3 style={{ color: '#34d399' }}>Smart Evaluation</h3>
            <p>Dynamic testing environment mimicking the real ISSB psychological and GTO tests.</p>
          </div>
        </div>
      </main>
    </div>
  );
}
