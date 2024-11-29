module.exports = {
  content: [
    "./src/**/*.{html,js,jsx,ts,tsx}",
  ],
  theme: {
    fontFamily: {
      sans: ['Kanit', 'regular', 'sans-serif'],
    },  
    extend: {
      colors: {
        'purple': '#6C63FF',
        'white': '#FFFFFF',
        'black': '#252525',
      },
    },
  },
  plugins: [
    require('daisyui'),
  ],
}