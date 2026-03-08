'use client';
import { useState } from 'react';
import { useRouter } from 'next/navigation';

export default function AdminLogin() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [code, setCode] = useState('');
    const [step, setStep] = useState(1);
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');
    const [loading, setLoading] = useState(false);
    const router = useRouter();

    const handleSendCode = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError('');

        try {
            const res = await fetch('/api/auth/dani/send', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });

            const data = await res.json();
            if (!res.ok) {
                setError(data.error || 'Verification failed');
            } else {
                setSuccess('Security code sent to email. (Check server logs in dev mode)');
                setStep(2);
            }
        } catch (err) {
            setError('An error occurred');
        }
        setLoading(false);
    };

    const handleVerifyCode = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError('');

        try {
            const res = await fetch('/api/auth/dani/verify', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, code })
            });

            const data = await res.json();
            if (!res.ok) {
                setError(data.error || 'Verification failed');
            } else {
                router.push('/dashboard/admin');
                router.refresh();
            }
        } catch (err) {
            setError('An error occurred');
        }
        setLoading(false);
    };

    return (
        <div className="container min-h-screen flex-center fade-in">
            <div className="glass-panel" style={{ width: '100%', maxWidth: '400px', borderTop: '4px solid var(--danger)' }}>
                <h2 style={{ textAlign: 'center', marginBottom: '2rem', color: 'var(--danger)' }}>Admin Portal</h2>

                {error && <div className="alert alert-error">{error}</div>}
                {success && <div className="alert alert-success">{success}</div>}

                {step === 1 ? (
                    <form onSubmit={handleSendCode}>
                        <div className="input-group">
                            <label className="input-label">Admin ID</label>
                            <input
                                type="email"
                                className="input-field"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                required
                            />
                        </div>

                        <div className="input-group">
                            <label className="input-label">Master Password</label>
                            <input
                                type="password"
                                className="input-field"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                required
                            />
                        </div>

                        <button type="submit" className="btn-primary" style={{ width: '100%', marginTop: '1rem', background: 'var(--danger)' }} disabled={loading}>
                            {loading ? 'Verifying...' : 'Request Security Code'}
                        </button>
                    </form>
                ) : (
                    <form onSubmit={handleVerifyCode}>
                        <div className="input-group">
                            <label className="input-label">6-Digit Security Code</label>
                            <input
                                type="text"
                                className="input-field"
                                value={code}
                                onChange={(e) => setCode(e.target.value)}
                                placeholder="000000"
                                maxLength={6}
                                required
                            />
                        </div>

                        <button type="submit" className="btn-primary" style={{ width: '100%', marginTop: '1rem', background: 'var(--success)' }} disabled={loading}>
                            {loading ? 'Authenticating...' : 'Complete Login'}
                        </button>
                    </form>
                )}
            </div>
        </div>
    );
}
