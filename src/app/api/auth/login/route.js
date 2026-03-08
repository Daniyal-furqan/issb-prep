import { db } from '@/lib/db';
import { signToken } from '@/lib/auth';
import { NextResponse } from 'next/server';

export async function POST(req) {
    try {
        const { email, password } = await req.json();

        const user = db.getUserByEmail(email);

        if (!user || user.password !== password) {
            return NextResponse.json({ error: 'Invalid credentials' }, { status: 401 });
        }

        if (!user.isApproved) {
            return NextResponse.json({ error: 'Your account is pending admin approval' }, { status: 403 });
        }

        // Sign JWT
        const token = signToken({ id: user.id, email: user.email, role: user.role });

        const response = NextResponse.json({ success: true, user: { email: user.email, role: user.role, name: user.name } });

        // Set cookie
        response.cookies.set('auth_token', token, {
            httpOnly: true,
            secure: process.env.NODE_ENV === 'production',
            sameSite: 'strict',
            maxAge: 7 * 24 * 60 * 60 // 7 days
        });

        return response;

    } catch (error) {
        return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
    }
}
