/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './templates/**/*.html',
        './news/templates/**/*.html',
        './accounts/templates/**/*.html',
        './static/**/*.js',
    ],
    darkMode: 'class',
    theme: {
        extend: {
            colors: {
                'dark-bg': '#1a1a1a',
                'dark-card': '#2a2a2a',
                'dark-text': '#e0e0e0',
                'dark-accent': '#4a90e2',
                'dark-border': '#3a3a3a',
            },
        },
    },
    plugins: [
        require('@tailwindcss/typography'),
    ],
}