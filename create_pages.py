import os

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>{title} | PlayGamio</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@600;700;800;900&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL,GRAD,opsz@400,1,0,20" rel="stylesheet" />
    <style>
        body {{
            font-family: 'Inter', sans-serif;
            background-color: #131230;
            background-image: linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
            background-size: 50px 50px;
            color: #fff;
            min-height: 100vh;
        }}
        .font-display {{ font-family: 'Outfit', sans-serif; }}
        .top-nav {{
            position: sticky;
            top: 0;
            z-index: 50;
            background-color: rgba(19, 18, 48, 0.85);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            padding: 8px 16px;
        }}
    </style>
</head>
<body>
    <!-- Top Navigation -->
    <nav class="top-nav flex items-center justify-between bg-gradient-to-r from-indigo-900 to-[#131230]">
        <div class="flex-1 flex items-center gap-3 sm:gap-6 overflow-hidden">
            <!-- Brand Logo -->
            <a href="/" class="flex items-center gap-2 shrink-0 group">
                <div class="bg-indigo-600 rounded-lg p-1.5 group-hover:bg-indigo-500 transition-colors">
                    <span class="material-symbols-outlined text-white" style="font-size: 20px;">sports_esports</span>
                </div>
                <span class="font-display font-bold text-xl tracking-tight">PlayGamio</span>
            </a>
            
            <div class="hidden sm:flex text-sm text-gray-400 font-semibold uppercase tracking-wider">
                {title}
            </div>
        </div>
    </nav>

    <main class="max-w-[800px] mx-auto px-4 py-12 min-h-[60vh]">
        <h1 class="font-display text-4xl font-bold mb-8">{title}</h1>
        <div class="prose prose-invert prose-lg text-gray-300">
            {content}
        </div>
    </main>

    <!-- Global Footer -->
    <footer class="bg-[#0b0a1c] border-t border-white/10 mt-12 py-12">
        <div class="max-w-[800px] mx-auto px-4 md:px-6 lg:px-8 text-center text-gray-500 text-sm">
            <p>&copy; 2026 PlayGamio. All rights reserved.</p>
            <div class="flex justify-center gap-4 mt-4 flex-wrap">
                <a href="/privacy.html" class="hover:text-indigo-400 transition-colors">Privacy</a>
                <a href="/terms.html" class="hover:text-indigo-400 transition-colors">Terms</a>
                <a href="/contact.html" class="hover:text-indigo-400 transition-colors">Contact</a>
                <a href="/about.html" class="hover:text-indigo-400 transition-colors">About</a>
                <a href="/affiliate.html" class="hover:text-indigo-400 transition-colors">Affiliate</a>
            </div>
        </div>
    </footer>
</body>
</html>
"""

pages = {
    "about.html": {
        "title": "About Us",
        "content": "<p>Welcome to PlayGamio, your ultimate destination for free 3D browser games. We believe that gaming should be accessible to everyone, without the need for high-end hardware or lengthy downloads.</p><p>Our mission is to curate the highest quality, most immersive web games available on the internet, optimized to run smoothly right from your browser.</p>"
    },
    "contact.html": {
        "title": "Contact Us",
        "content": "<p>If you have any questions, suggestions, or concerns regarding PlayGamio, please do not hesitate to contact us.</p><p>Email: <strong>support@playgamio.com</strong></p><p>We strive to respond to all inquiries within 48 hours.</p>"
    },
    "privacy.html": {
        "title": "Privacy Policy",
        "content": "<p>At PlayGamio, we prioritize the privacy of our visitors. This Privacy Policy document contains types of information that is collected and recorded by PlayGamio and how we use it.</p><h2>Cookies and Web Beacons</h2><p>Like any other website, PlayGamio uses 'cookies'. These cookies are used to store information including visitors' preferences, and the pages on the website that the visitor accessed or visited. The information is used to optimize the users' experience by customizing our web page content based on visitors' browser type and/or other information.</p><h2>Google DoubleClick DART Cookie</h2><p>Google is one of a third-party vendor on our site. It also uses cookies, known as DART cookies, to serve ads to our site visitors based upon their visit to www.website.com and other sites on the internet. However, visitors may choose to decline the use of DART cookies by visiting the Google ad and content network Privacy Policy at the following URL – https://policies.google.com/technologies/ads</p><h2>Our Advertising Partners</h2><p>Some of advertisers on our site may use cookies and web beacons. Our advertising partners include Google AdSense.</p>"
    },
    "terms.html": {
        "title": "Terms of Service",
        "content": "<p>These terms and conditions outline the rules and regulations for the use of PlayGamio's Website.</p><p>By accessing this website we assume you accept these terms and conditions. Do not continue to use PlayGamio if you do not agree to take all of the terms and conditions stated on this page.</p><p>Unless otherwise stated, PlayGamio and/or its licensors own the intellectual property rights for all material on PlayGamio. All intellectual property rights are reserved.</p>"
    },
    "affiliate.html": {
        "title": "Affiliate Disclosure",
        "content": "<p>PlayGamio believes in full transparency. This Affiliate Disclosure details affiliate relationships that PlayGamio has with other companies and products.</p><p>Some of the links on this website are affiliate links. This means if you click on the link and purchase the item, we will receive an affiliate commission at no extra cost to you. We only recommend products or services we believe will add value to our readers and gamers.</p>"
    }
}

for filename, data in pages.items():
    filepath = os.path.join('/root/playgamio/html', filename)
    with open(filepath, 'w') as f:
        f.write(html_template.format(title=data["title"], content=data["content"]))
    print(f"Created {filename}")
