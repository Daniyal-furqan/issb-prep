'use client';
import Link from 'next/link';

export default function DashboardLayout({ children }) {
    return (
        <div className="layout-wrapper flex">
            <aside className="sidebar">
                <div className="nav-brand">
                    <span style={{ color: 'var(--accent-color)' }}>✦</span> ISSB Pro
                </div>

                <nav className="sidebar-nav">
                    <Link href="/dashboard" className="sidebar-link">
                        <span>●</span> Dashboard Home
                    </Link>
                    <Link href="/dashboard/introduction" className="sidebar-link">
                        <span>●</span> Introduction
                    </Link>
                    <Link href="/dashboard/preparation" className="sidebar-link">
                        <span>●</span> Preparation
                    </Link>
                    <Link href="/dashboard/test" className="sidebar-link">
                        <span>●</span> Online Test
                    </Link>
                    <div style={{ marginTop: 'auto', paddingTop: '2rem' }}>
                        <Link href="/dashboard/admin" className="sidebar-link" style={{ color: 'var(--danger)' }}>
                            <span>⚙</span> Admin Panel
                        </Link>
                        <button className="btn-secondary" style={{ width: '100%', marginTop: '1rem', textAlign: 'center' }} onClick={() => {
                            document.cookie = 'auth_token=; path=/; expires=Thu, 01 Jan 1970 00:00:01 GMT';
                            window.location.href = '/login';
                        }}>
                            Logout
                        </button>
                    </div>
                </nav>
            </aside>

            <main className="main-content fade-in">
                {children}
            </main>
        </div>
    );
}
