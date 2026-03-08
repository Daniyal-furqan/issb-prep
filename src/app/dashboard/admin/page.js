'use client';
import { useState, useEffect } from 'react';

export default function AdminDashboard() {
    const [users, setUsers] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    const fetchUsers = async () => {
        try {
            setLoading(true);
            const res = await fetch('/api/admin/users');
            const data = await res.json();
            if (res.ok) {
                setUsers(data.users || []);
            } else {
                setError(data.error || 'Failed to fetch users');
            }
        } catch {
            setError('An error occurred');
        }
        setLoading(false);
    };

    useEffect(() => {
        fetchUsers();
    }, []);

    const toggleApproval = async (email, currentStatus) => {
        try {
            const res = await fetch('/api/admin/users/approve', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, approve: !currentStatus })
            });
            if (res.ok) fetchUsers();
        } catch (err) {
            console.error(err);
        }
    };

    return (
        <div>
            <h1 style={{ color: 'var(--danger)', marginBottom: '2rem' }}>Admin Control Panel</h1>

            {error && <div className="alert alert-error">{error}</div>}

            {loading ? (
                <p>Loading users...</p>
            ) : (
                <div className="glass-panel" style={{ padding: '0', overflow: 'hidden' }}>
                    <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
                        <thead>
                            <tr style={{ background: 'rgba(255,255,255,0.05)', borderBottom: '1px solid var(--glass-border)' }}>
                                <th style={{ padding: '1rem' }}>Name</th>
                                <th style={{ padding: '1rem' }}>Email</th>
                                <th style={{ padding: '1rem' }}>Status</th>
                                <th style={{ padding: '1rem' }}>Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            {users.map(u => (
                                <tr key={u.id} style={{ borderBottom: '1px solid var(--glass-border)' }}>
                                    <td style={{ padding: '1rem' }}>{u.name}</td>
                                    <td style={{ padding: '1rem', color: 'var(--text-secondary)' }}>{u.email}</td>
                                    <td style={{ padding: '1rem' }}>
                                        <span style={{
                                            padding: '0.25rem 0.75rem',
                                            borderRadius: '999px',
                                            fontSize: '0.875rem',
                                            background: u.isApproved ? 'rgba(16, 185, 129, 0.2)' : 'rgba(239, 68, 68, 0.2)',
                                            color: u.isApproved ? 'var(--success)' : 'var(--danger)'
                                        }}>
                                            {u.isApproved ? 'Approved' : 'Pending'}
                                        </span>
                                    </td>
                                    <td style={{ padding: '1rem' }}>
                                        <button
                                            className="btn-secondary"
                                            style={{ fontSize: '0.875rem', padding: '0.5rem 1rem' }}
                                            onClick={() => toggleApproval(u.email, u.isApproved)}
                                        >
                                            {u.isApproved ? 'Revoke Access' : 'Approve Login'}
                                        </button>
                                    </td>
                                </tr>
                            ))}
                            {users.length === 0 && (
                                <tr>
                                    <td colSpan={4} style={{ padding: '2rem', textAlign: 'center', color: 'var(--text-secondary)' }}>
                                        No users found.
                                    </td>
                                </tr>
                            )}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
}
