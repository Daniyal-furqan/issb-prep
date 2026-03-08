// src/lib/db.js
// Temporary In-Memory Database for Vercel Hobby tier / Local testing

// Admin credentials
export const ADMIN_EMAIL = 'digidaniyal@gmail.com';
export const ADMIN_PASS = 'D@niy@l001$';

if (!global.users) {
    global.users = [
        {
            id: "admin_1",
            email: ADMIN_EMAIL,
            password: ADMIN_PASS,
            role: 'admin',
            isApproved: true,
            name: "Daniyal"
        }
    ];
}

if (!global.verificationCodes) {
    global.verificationCodes = {};
}

export const db = {
    getUsers: () => global.users,
    addUser: (user) => {
        global.users.push(user);
        return user;
    },
    getUserByEmail: (email) => global.users.find(u => u.email === email),
    updateUser: (email, updates) => {
        const idx = global.users.findIndex(u => u.email === email);
        if (idx !== -1) {
            global.users[idx] = { ...global.users[idx], ...updates };
            return true;
        }
        return false;
    },
    deleteUser: (email) => {
        global.users = global.users.filter(u => u.email !== email);
    },

    // 2FA Methods
    save2FACode: (email, code) => {
        global.verificationCodes[email] = {
            code,
            expires: Date.now() + 5 * 60 * 1000 // 5 minutes
        };
    },
    verify2FACode: (email, code) => {
        const record = global.verificationCodes[email];
        if (record && record.code === code && record.expires > Date.now()) {
            delete global.verificationCodes[email];
            return true;
        }
        return false;
    }
};
