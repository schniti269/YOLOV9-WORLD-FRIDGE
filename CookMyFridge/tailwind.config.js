/** @type {import('tailwindcss').Config} */
export default {
    content: ['./src/**/*.{html,svelte,css,js,ts}', './node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}'],
    plugins: [require('flowbite/plugin')],
    darkMode: 'class',
    theme: {
        extend: {
            colors: {
                'background': {
                    DEFAULT: '#131515',
                    100: '#040404',
                    200: '#080909',
                    300: '#0c0d0d',
                    400: '#101111',
                    500: '#131515',
                    600: '#404747',
                    700: '#6d7878',
                    800: '#9ca6a6',
                    900: '#ced2d2'
                },
                'primary': {
                    DEFAULT: '#2b2c28',
                    100: '#080908',
                    200: '#111110',
                    300: '#191a17',
                    400: '#21221f',
                    500: '#2b2c28',
                    600: '#56584f',
                    700: '#828578',
                    800: '#abaea5',
                    900: '#d5d6d2'
                },
                'secondary': {
                    DEFAULT: '#339989',
                    100: '#0a1f1c',
                    200: '#143d37',
                    300: '#1f5c53',
                    400: '#297a6e',
                    500: '#339989',
                    600: '#47c2af',
                    700: '#75d1c3',
                    800: '#a3e0d7',
                    900: '#d1f0eb'
                },
                'accent': {
                    DEFAULT: '#7de2d1',
                    100: '#0d3a32',
                    200: '#197364',
                    300: '#26ad97',
                    400: '#44d6be',
                    500: '#7de2d1',
                    600: '#97e8db',
                    700: '#b1eee4',
                    800: '#cbf4ed',
                    900: '#e5f9f6'
                }
            }
        },
    },
}

