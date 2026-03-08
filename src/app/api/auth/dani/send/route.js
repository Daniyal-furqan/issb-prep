import { db, ADMIN_EMAIL, ADMIN_PASS } from '@/lib/db';
import { NextResponse } from 'next/server';

export async function POST(req) {
    try {
        const { email, password } = await req.json();

        if (email !== ADMIN_EMAIL || password !== ADMIN_PASS) {
            return NextResponse.json({ error: 'Invalid admin credentials' }, { status: 401 });
        }

        // Generate 6 digit code
        const code = Math.floor(100000 + Math.random() * 900000).toString();

        // Save to DB
        db.save2FACode(email, code);

        // Simulated email sending (In production, replace with Nodemailer/Resend)
        console.log('\n=============================================');
        console.log(`[SIMULATED EMAIL] To: ${email}`);
        console.log(`Subject: Your ISSB Pro Admin 2FA Code`);
        console.log(`Code: ${code}`);
        console.log('=============================================\n');

        return NextResponse.json({ success: true, message: '2FA code sent to your email.' });

    } catch (error) {
        return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
    }
}
