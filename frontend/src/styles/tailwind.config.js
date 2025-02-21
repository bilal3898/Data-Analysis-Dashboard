/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./src/**/*.{js,jsx,ts,tsx}"],
    darkMode: "class",
    theme: {
      extend: {
        colors: {
          primary: "#4F46E5",
          secondary: "#64748B",
          accent: "#F97316",
          background: "#F9FAFB",
          darkBackground: "#1E293B",
        },
        fontFamily: {
          sans: ["Inter", "sans-serif"],
        },
      },
    },
    plugins: [],
  };
  