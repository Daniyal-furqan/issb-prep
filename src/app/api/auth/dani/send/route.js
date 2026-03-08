import { db, ADMIN_EMAIL, ADMIN_PASS } from '@/lib/db';
import { NextResponse } from 'next/server';
import nodemailer from 'nodemailer';

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

        // Setup Nodemailer transporter
        const transporter = nodemailer.createTransport({
            service: 'gmail',
            auth: {
                user: process.env.EMAIL_USER,
                pass: process.env.EMAIL_PASS
            }
        });

        // Send Real Email
        const mailOptions = {
            from: process.env.EMAIL_USER,
            to: email,
            subject: 'Your ISSB Pro Admin 2FA Code',
            text: `Your admin login security code for ISSB Pro is: ${code}\n\nThis code will expire in 5 minutes.`
        };

        await transporter.sendMail(mailOptions);

        return NextResponse.json({ success: true, message: '2FA code sent to your email.' });

    } catch (error) {
        return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
    }
}
