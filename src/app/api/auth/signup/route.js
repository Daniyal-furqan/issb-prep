import { db } from '@/lib/db';
import { NextResponse } from 'next/server';

export async function POST(req) {
    try {
        const { name, email, password } = await req.json();

        if (!name || !email || !password) {
            return NextResponse.json({ error: 'Missing fields' }, { status: 400 });
        }

        if (db.getUserByEmail(email)) {
            return NextResponse.json({ error: 'User already exists' }, { status: 400 });
        }

        const user = {
            id: Date.now().toString(),
            name,
            email,
            password,
            role: 'user',
            isApproved: false // Requires admin approval, as requested
        };

        db.addUser(user);

        return NextResponse.json({ success: true, message: 'Signup successful. Waiting for admin approval.' });

    } catch (error) {
        return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
    }
}
