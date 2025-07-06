module.exports = {
  darkMode: "class",
  content: [
    "../templates/**/*.html",
    "./flowbite/**/*.js",
    "../../templates/**/*.html",
    "../../**/templates/**/*.html",
  ],
  theme: {
    extend: {
      colors: {
        // Primary color scale - refined orange palette with better accessibility
        primary: {
          50: "#fff8f0", // Lightest warm white
          100: "#ffedd5", // Soft peach
          200: "#ffe0b5", // Light orange
          300: "#ffcc80", // Muted orange
          400: "#ffb347", // Vibrant orange (secondary accent)
          500: "#ff9800", // Balanced primary orange (WCAG compliant)
          600: "#f57c00", // Deep orange (buttons/hover)
          700: "#e65100", // Rich orange (important elements)
          800: "#bf360c", // Dark orange
          900: "#8d2b0b", // Deep sophisticated orange
          DEFAULT: "#ff9800", // Material Design standard orange
        },

        scrollbar: {
          bg: "#fac89600",
          color: "#ff960061",
        },

        // Secondary color - complementary teal for balance
        secondary: {
          50: "#e0f7fa",
          100: "#b2ebf2",
          200: "#80deea",
          300: "#4dd0e1",
          400: "#26c6da",
          500: "#00bcd4",
          600: "#00acc1",
          700: "#0097a7",
          800: "#00838f",
          900: "#006064",
        },

        // Text colors - optimized for readability
        text: {
          100: "#212121", // High contrast (WCAG AAA)
          200: "#424242", // Secondary text
          300: "#757575", // Tertiary text
          400: "#bdbdbd", // Disabled text
        },

        // Background colors - subtle warmth
        bg: {
          100: "#ffffff", // Pure white
          200: "#faf5f0", // Warm white
          300: "#f5f5f5", // Neutral white
          400: "#eeeeee", // Light gray
          500: "lightgray", // Light gray
        },

        // Semantic colors
        success: "#4caf50",
        warning: "#ffc107",
        error: "#f44336",
        info: "#2196f3",

        // Theme-specific colors
        light: {
          card: "#ffffff",
          background: "#faf5f0", // Warm subtle background
          text: "#212121",
          border: "#e0e0e0", // Softer border
          glass: "rgba(255, 255, 255, 0.85)", // More opaque for readability
          overlay: "rgba(0, 0, 0, 0.08)", // Subtle overlay
        },
        dark: {
          card: "#1e1e1e", // True dark instead of blue-ish
          background: "#121212", // Deep dark
          text: "#f5f5f5",
          border: "#424242",
          glass: "rgba(30, 30, 30, 0.85)",
          overlay: "rgba(255, 255, 255, 0.08)",
        },
      },

      // Additional theme enhancements
      boxShadow: {
        glass: "0 4px 30px rgba(0, 0, 0, 0.1)",
        "glass-dark": "0 4px 30px rgba(0, 0, 0, 0.3)",
      },
      backdropBlur: {
        glass: "8px",
      },
    },
  },
  plugins: [
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
    require("@tailwindcss/aspect-ratio"),
    require("flowbite/plugin"),
  ],
};
