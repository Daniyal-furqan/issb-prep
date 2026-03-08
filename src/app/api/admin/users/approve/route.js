import { db } from '@/lib/db';
import { verifyToken } from '@/lib/auth';
import { NextResponse } from 'next/server';

export async function POST(req) {
    try {
        const authCookie = req.cookies.get('auth_token')?.value;
        if (!authCookie) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });

        const tokenData = verifyToken(authCookie);
        if (!tokenData || tokenData.role !== 'admin') {
            return NextResponse.json({ error: 'Unauthorized. Admin strictly.' }, { status: 403 });
        }

        const { email, approve } = await req.json();

        if (!email) {
            return NextResponse.json({ error: 'Email required' }, { status: 400 });
        }

        const updated = db.updateUser(email, { isApproved: approve });

        if (updated) {
            return NextResponse.json({ success: true, message: `User ${approve ? 'approved' : 'revoked'}.` });
        } else {
            return NextResponse.json({ error: 'User not found' }, { status: 404 });
        }

    } catch (error) {
        return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
    }
}
