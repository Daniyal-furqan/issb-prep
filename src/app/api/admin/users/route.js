import { db } from '@/lib/db';
import { verifyToken } from '@/lib/auth';
import { NextResponse } from 'next/server';

export async function GET(req) {
    try {
        const authCookie = req.cookies.get('auth_token')?.value;
        if (!authCookie) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });

        const tokenData = verifyToken(authCookie);
        if (!tokenData || tokenData.role !== 'admin') {
            return NextResponse.json({ error: 'Unauthorized. Admin strictly.' }, { status: 403 });
        }

        // Return all users except admin
        const users = db.getUsers().filter(u => u.role !== 'admin');

        return NextResponse.json({ users });

    } catch (error) {
        return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
    }
}
