import os
import re

# List of page files to update
page_files = [
    'pages/artificial_intelligence.html',
    'pages/computer_science.html',
    'pages/computer_vision.html',
    'pages/data_science.html',
    'pages/information_system.html',
    'pages/knowledge_engineer.html',
    'pages/computer_network.html',
    'pages/software_engineer.html'
]

# Enhanced responsive CSS template
responsive_css_template = """
		/* Enhanced responsive design - Does not affect export PNG */
		@media (max-width: 1024px) {
			body:not(.export-mode) #infographic-content {
				padding: 1rem !important;
			}

			body:not(.export-mode) .header-bg {
				padding: 3rem 1rem !important;
			}

			body:not(.export-mode) .header-content h1 {
				font-size: 2rem !important;
				line-height: 1.2 !important;
			}

			body:not(.export-mode) .major {
				font-size: 2rem !important;
			}

			body:not(.export-mode) .english {
				font-size: 1.25rem !important;
			}

			body:not(.export-mode) .major-slogan {
				font-size: 1.25rem !important;
			}

			body:not(.export-mode) .grid {
				grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) !important;
				gap: 1rem !important;
			}

			body:not(.export-mode) .section-title {
				font-size: 1.75rem !important;
			}

			body:not(.export-mode) main {
				padding: 1rem !important;
			}

			body:not(.export-mode) section {
				margin: 2rem 0 !important;
			}
		}

		@media (max-width: 768px) {
			body:not(.export-mode) .header-bg {
				padding: 2rem 0.75rem !important;
			}

			body:not(.export-mode) .header-content h1 {
				font-size: 1.5rem !important;
			}

			body:not(.export-mode) .major {
				font-size: 1.5rem !important;
			}

			body:not(.export-mode) .english {
				font-size: 1rem !important;
			}

			body:not(.export-mode) .major-slogan {
				font-size: 1rem !important;
			}

			body:not(.export-mode) .faculty-slogan {
				font-size: 1rem !important;
			}

			body:not(.export-mode) .grid {
				grid-template-columns: 1fr !important;
				gap: 0.75rem !important;
			}

			body:not(.export-mode) .section-title {
				font-size: 1.5rem !important;
			}

			body:not(.export-mode) .card {
				padding: 1rem !important;
			}

			body:not(.export-mode) .card h3 {
				font-size: 1.125rem !important;
			}

			body:not(.export-mode) .card p {
				font-size: 0.875rem !important;
			}
		}

		@media (max-width: 640px) {
			body:not(.export-mode) #infographic-content {
				padding: 0.5rem !important;
			}

			body:not(.export-mode) .header-bg {
				padding: 1.5rem 0.5rem !important;
			}

			body:not(.export-mode) .header-content h1 {
				font-size: 1.25rem !important;
			}

			body:not(.export-mode) .major {
				font-size: 1.25rem !important;
			}

			body:not(.export-mode) .english {
				font-size: 0.875rem !important;
			}

			body:not(.export-mode) .major-slogan {
				font-size: 0.875rem !important;
			}

			body:not(.export-mode) .faculty {
				font-size: 0.75rem !important;
			}

			body:not(.export-mode) .faculty-slogan {
				font-size: 0.875rem !important;
			}

			body:not(.export-mode) .section-title {
				font-size: 1.25rem !important;
			}

			body:not(.export-mode) main {
				padding: 0.75rem !important;
			}

			body:not(.export-mode) section {
				margin: 1.5rem 0 !important;
			}

			body:not(.export-mode) .card {
				padding: 0.75rem !important;
			}

			body:not(.export-mode) .card h3 {
				font-size: 1rem !important;
			}

			body:not(.export-mode) .card p {
				font-size: 0.8rem !important;
			}

			body:not(.export-mode) .icon {
				width: 32px !important;
				height: 32px !important;
			}
		}"""

for file_path in page_files:
    print(f"Processing {file_path}...")
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the position to insert CSS (before </style>)
    style_end_pattern = r'(\s*}\s*</style>\s*</head>)'
    
    # Insert the responsive CSS before </style>
    new_content = re.sub(
        style_end_pattern,
        responsive_css_template + r'\1',
        content,
        count=1
    )
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Updated {file_path}")

print("\n🎉 All files updated with responsive design!")
