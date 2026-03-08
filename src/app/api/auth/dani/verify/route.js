import { db, ADMIN_EMAIL } from '@/lib/db';
import { signToken } from '@/lib/auth';
import { NextResponse } from 'next/server';

export async function POST(req) {
    try {
        const { email, code } = await req.json();

        if (email !== ADMIN_EMAIL) {
            return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
        }

        const isValid = db.verify2FACode(email, code);

        if (!isValid) {
            return NextResponse.json({ error: 'Invalid or expired 2FA code' }, { status: 401 });
        }

        const adminUser = db.getUserByEmail(email);

        // Sign JWT
        const token = signToken({ id: adminUser.id, email: adminUser.email, role: adminUser.role });

        const response = NextResponse.json({ success: true, user: { email: adminUser.email, role: adminUser.role, name: adminUser.name } });

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
