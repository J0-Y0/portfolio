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
        // Primary color scale - professional blue palette
        primary: {
          50: "#f0f4ff",
          100: "#dbe6fe",
          200: "#bfd3fe",
          300: "#93b5fd",
          400: "#6090fa",
          500: "#3b76f6", // Main primary blue
          600: "#2659e8",
          700: "#1d44d5",
          800: "#1e38ac",
          900: "#1e3287",
          DEFAULT: "#3b76f6",
        },

        // Secondary color - slate gray for balance
        secondary: {
          50: "#f8fafc",
          100: "#f1f5f9",
          200: "#e2e8f0",
          300: "#cbd5e1",
          400: "#94a3b8",
          500: "#64748b",
          600: "#475569",
          700: "#334155",
          800: "#1e293b",
          900: "#0f172a",
        },

        // Text colors - optimized for readability
        text: {
          100: "#1e293b", // Dark slate for primary text
          200: "#475569", // Secondary text
          300: "#64748b", // Tertiary text
          400: "#94a3b8", // Disabled text
        },

        // Background colors - clean whites and grays
        bg: {
          100: "#ffffff", // Pure white
          200: "#f8fafc", // Lightest gray
          300: "#f1f5f9", // Very light gray
          400: "#e2e8f0", // Light gray
        },

        // Semantic colors
        success: "#10b981", // Emerald green
        warning: "#f59e0b", // Amber
        error: "#ef4444", // Red
        info: "#3b82f6", // Blue

        // Theme-specific colors
        light: {
          card: "#ffffff",
          background: "#f8fafc", // Very light gray
          text: "#1e293b", // Dark slate
          border: "#e2e8f0", // Light gray
          glass: "rgba(255, 255, 255, 0.9)",
          overlay: "rgba(0, 0, 0, 0.05)",
        },
        dark: {
          card: "#1e293b", // Dark slate
          background: "#0f172a", // Very dark slate
          text: "#f8fafc", // Very light gray
          border: "#334155", // Medium slate
          glass: "rgba(30, 41, 59, 0.9)",
          overlay: "rgba(255, 255, 255, 0.05)",
        },
      },
      // Additional theme enhancements
      boxShadow: {
        glass: "0 4px 20px rgba(0, 0, 0, 0.08)",
        "glass-dark": "0 4px 20px rgba(0, 0, 0, 0.2)",
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
