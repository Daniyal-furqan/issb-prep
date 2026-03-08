import { ADMIN_EMAIL, ADMIN_PASS } from '@/lib/db';
import { signToken } from '@/lib/auth';
import { NextResponse } from 'next/server';

export async function POST(req) {
    try {
        const { email, password } = await req.json();

        if (email !== ADMIN_EMAIL || password !== ADMIN_PASS) {
            return NextResponse.json({ error: 'Invalid admin credentials' }, { status: 401 });
        }

        // Bypassing 2FA logic to allow immediate access for the user.
        // Direct login token generation:
        const token = signToken({ id: 'admin_1', email: ADMIN_EMAIL, role: 'admin' });

        const response = NextResponse.json({ success: true, message: 'Login successful.', user: { email: ADMIN_EMAIL, role: 'admin', name: 'Daniyal' } });

        response.cookies.set('auth_token', token, {
            httpOnly: true,
            secure: process.env.NODE_ENV === 'production',
            sameSite: 'strict',
            maxAge: 7 * 24 * 60 * 60 // 7 days
        });

        return response;

    } catch (error) {
        console.error('Login error:', error);
        return NextResponse.json({ error: 'Internal Server Error during direct login' }, { status: 500 });
    }
}
