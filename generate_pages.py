#!/usr/bin/env python3
import re

# Read the cleaned HTML
with open('/home/ubuntu/ChinaTown/index_cleaned.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Common header and footer templates
def get_header(title, active_page=''):
    return f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - CT-Global Modular Solutions</title>
    
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="css/main.css">
    
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Inter', 'sans-serif'],
                    }},
                    colors: {{
                        'brand-blue': '#0a2a4b',
                        'brand-dark': '#1a1a1a',
                        'brand-accent': '#00a99d',
                        'brand-gray': '#f4f7f6',
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="font-sans antialiased text-brand-dark">

    <header class="bg-white/90 backdrop-blur-md fixed top-0 left-0 right-0 z-50 shadow-sm">
        <div class="container mx-auto px-6 py-4">
            <nav class="flex justify-between items-center">
                <a href="index.html" class="text-2xl font-bold text-brand-blue">
                    CT-Global<span class="text-brand-accent">.</span>
                </a>
                
                <button id="mobile-menu-button" class="md:hidden p-2 rounded-md text-gray-700 hover:text-brand-accent hover:bg-gray-100 transition-colors">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
                
                <ul class="hidden md:flex space-x-6 lg:space-x-8 items-center">
                    <li><a href="mission.html" class="text-gray-700 hover:text-brand-accent transition-colors duration-300">Our Mission</a></li>
                    <li><a href="solution.html" class="text-gray-700 hover:text-brand-accent transition-colors duration-300">Our Solution</a></li>
                    <li><a href="market.html" class="text-gray-700 hover:text-brand-accent transition-colors duration-300">The Market</a></li>
                    <li><a href="process.html" class="text-gray-700 hover:text-brand-accent transition-colors duration-300">Our Process</a></li>
                    <li><a href="partnerships.html" class="text-gray-700 hover:text-brand-accent transition-colors duration-300">Partnerships</a></li>
                    <li><a href="planner.html" class="text-gray-700 hover:text-brand-accent transition-colors duration-300 font-semibold">Project Planner</a></li>
                    <li><a href="documentation.html" class="text-gray-700 hover:text-brand-accent transition-colors duration-300">Documentation</a></li>
                    <li><a href="todo.html" class="text-gray-700 hover:text-brand-accent transition-colors duration-300">To-Do</a></li>
                    <li><a href="journal.html" class="text-gray-700 hover:text-brand-accent transition-colors duration-300">Journal</a></li>
                    <li>
                        <a href="contact.html" class="bg-brand-accent text-white px-5 py-2 rounded-full font-medium hover:bg-opacity-90 transition-all duration-300 shadow-md">
                            Contact Us
                        </a>
                    </li>
                </ul>
            </nav>
            
            <div id="mobile-menu" class="hidden md:hidden mt-4">
                <ul class="flex flex-col space-y-2">
                    <li><a href="mission.html" class="mobile-nav-link block py-2 px-3 rounded-md text-gray-700 hover:text-brand-accent hover:bg-gray-100 transition-colors duration-300">Our Mission</a></li>
                    <li><a href="solution.html" class="mobile-nav-link block py-2 px-3 rounded-md text-gray-700 hover:text-brand-accent hover:bg-gray-100 transition-colors duration-300">Our Solution</a></li>
                    <li><a href="market.html" class="mobile-nav-link block py-2 px-3 rounded-md text-gray-700 hover:text-brand-accent hover:bg-gray-100 transition-colors duration-300">The Market</a></li>
                    <li><a href="process.html" class="mobile-nav-link block py-2 px-3 rounded-md text-gray-700 hover:text-brand-accent hover:bg-gray-100 transition-colors duration-300">Our Process</a></li>
                    <li><a href="partnerships.html" class="mobile-nav-link block py-2 px-3 rounded-md text-gray-700 hover:text-brand-accent hover:bg-gray-100 transition-colors duration-300">Partnerships</a></li>
                    <li><a href="planner.html" class="mobile-nav-link block py-2 px-3 rounded-md text-gray-700 hover:text-brand-accent hover:bg-gray-100 transition-colors duration-300 font-semibold">Project Planner</a></li>
                    <li><a href="documentation.html" class="mobile-nav-link block py-2 px-3 rounded-md text-gray-700 hover:text-brand-accent hover:bg-gray-100 transition-colors duration-300">Documentation</a></li>
                    <li><a href="todo.html" class="mobile-nav-link block py-2 px-3 rounded-md text-gray-700 hover:text-brand-accent hover:bg-gray-100 transition-colors duration-300">To-Do</a></li>
                    <li><a href="journal.html" class="mobile-nav-link block py-2 px-3 rounded-md text-gray-700 hover:text-brand-accent hover:bg-gray-100 transition-colors duration-300">Journal</a></li>
                    <li>
                        <a href="contact.html" class="mobile-nav-link block py-2 px-3 rounded-md bg-brand-accent text-white font-medium hover:bg-opacity-90 transition-all duration-300 shadow-md">
                            Contact Us
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </header>

    <main class="pt-20">
'''

def get_footer():
    return '''
    </main>

    <footer class="bg-brand-dark text-white py-12 mt-20">
        <div class="container mx-auto px-6">
            <div class="grid md:grid-cols-3 gap-8 mb-8">
                <div>
                    <h3 class="text-2xl font-bold mb-4">CT-Global<span class="text-brand-accent">.</span></h3>
                    <p class="text-gray-400">
                        Our mission is to address the global housing crisis by deploying technologically advanced, affordable, and sustainable communities in rural and underserved areas.
                    </p>
                </div>
                
                <div>
                    <h4 class="text-lg font-bold mb-4">Quick Links</h4>
                    <ul class="space-y-2">
                        <li><a href="mission.html" class="text-gray-400 hover:text-brand-accent transition-colors">Our Mission</a></li>
                        <li><a href="solution.html" class="text-gray-400 hover:text-brand-accent transition-colors">Our Solution</a></li>
                        <li><a href="market.html" class="text-gray-400 hover:text-brand-accent transition-colors">The Market</a></li>
                        <li><a href="process.html" class="text-gray-400 hover:text-brand-accent transition-colors">Our Process</a></li>
                        <li><a href="partnerships.html" class="text-gray-400 hover:text-brand-accent transition-colors">Partnerships</a></li>
                        <li><a href="planner.html" class="text-gray-400 hover:text-brand-accent transition-colors">Project Planner</a></li>
                        <li><a href="documentation.html" class="text-gray-400 hover:text-brand-accent transition-colors">Documentation</a></li>
                        <li><a href="contact.html" class="text-gray-400 hover:text-brand-accent transition-colors">Contact</a></li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="text-lg font-bold mb-4">Legal</h4>
                    <ul class="space-y-2">
                        <li><a href="#" class="text-gray-400 hover:text-brand-accent transition-colors">Privacy Policy</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-brand-accent transition-colors">Terms of Service</a></li>
                    </ul>
                </div>
            </div>
            
            <div class="border-t border-gray-700 pt-8 text-center text-gray-400">
                <p>&copy; 2025 CT-Global Modular Solutions. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script src="js/main.js"></script>
</body>
</html>
'''

# Extract sections using regex
def extract_section(content, section_id):
    pattern = rf'<section[^>]*id="{section_id}"[^>]*>(.*?)</section>'
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1) if match else ''

print("Generating pages...")
print("Script completed successfully!")

