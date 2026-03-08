export default function IntroductionPage() {
    const schedule = [
        {
            day: "Arrival Day",
            tasks: [
                "Biodata form (4 times)",
                "Essay writing"
            ]
        },
        {
            day: "1st Day",
            tasks: [
                "Mechanical aptitude test",
                "Sentence completion test",
                "Word association test",
                "Picture story",
                "Pointer story",
                "Self description test",
                "Situation reaction test",
                "Opi"
            ]
        },
        {
            day: "2nd Day",
            subtitle: "(Indoor & Outdoor)",
            tasks: [
                "Public speaking / Lecturate",
                "Military planning",
                "Progressive group task",
                "Half group task",
                "Half group race",
                "Group discussion",
                "Deputy interview"
            ]
        },
        {
            day: "3rd Day",
            tasks: [
                "Individual Obstacles",
                "Command Task",
                "Mutual assessment test"
            ]
        },
        {
            day: "Departure Day",
            tasks: [
                "Re interviews",
                "Re obstacles",
                "Re command tasks"
            ]
        }
    ];

    return (
        <div>
            <h1 style={{ color: 'var(--accent-color)', marginBottom: '2rem' }}>ISSB Schedule</h1>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem', position: 'relative' }}>
                {/* Timeline Line */}
                <div style={{
                    position: 'absolute',
                    left: '24px',
                    top: '0',
                    bottom: '0',
                    width: '2px',
                    background: 'var(--glass-border)',
                    zIndex: '0'
                }}></div>

                {schedule.map((item, index) => (
                    <div key={index} style={{ display: 'flex', gap: '2rem', position: 'relative', zIndex: '1' }}>
                        <div style={{
                            width: '50px',
                            height: '50px',
                            borderRadius: '50%',
                            background: 'var(--bg-color)',
                            border: '2px solid var(--accent-color)',
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'center',
                            fontWeight: 'bold',
                            boxShadow: '0 0 15px var(--accent-glow)'
                        }}>
                            {index + 1}
                        </div>

                        <div className="glass-panel" style={{ flex: '1' }}>
                            <div style={{ display: 'flex', alignItems: 'baseline', gap: '1rem', marginBottom: '1rem' }}>
                                <h2 style={{ color: 'white', margin: 0 }}>{item.day}</h2>
                                {item.subtitle && <span style={{ color: 'var(--text-secondary)' }}>{item.subtitle}</span>}
                            </div>

                            <ul style={{ listStyleType: 'none', display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
                                {item.tasks.map((task, i) => (
                                    <li key={i} style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
                                        <span style={{ color: '#10b981' }}>✓</span> {task}
                                    </li>
                                ))}
                            </ul>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}
