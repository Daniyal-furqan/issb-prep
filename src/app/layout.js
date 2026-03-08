import './globals.css';

export const metadata = {
  title: 'ISSB AI Preparation - Premium Platform',
  description: 'AI-powered psychologist and leader for your ISSB preparation.',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <main>{children}</main>
      </body>
    </html>
  );
}
