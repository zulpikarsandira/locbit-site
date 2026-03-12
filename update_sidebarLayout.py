import os
from bs4 import BeautifulSoup

def update_sidebar_layout(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # 1. Update Layout structure First
    nav_grid = soup.find('div', class_='nav-grid')
    if nav_grid:
        nav_right = nav_grid.find('div', class_='nav-right')
        
        if nav_right:
            # Check if it's already updated (contains sub columns)
            if nav_right.find('div', class_='nav-col-left'):
                print(f"[{os.path.basename(html_path)}] Sidebar structure already updated. Skipping layout change.")
            else:
                links = nav_right.find_all('a', class_='nav-link-block', recursive=False)
                dividers = nav_right.find_all('div', class_='devider-line', recursive=False)
                
                # We expect 8 links total: 4 on the left, 4 on the right
                if len(links) >= 8:
                    left_links = links[:4]
                    right_links = links[4:]
                    
                    # Create two column containers
                    left_col = soup.new_tag('div', attrs={'class': 'nav-col nav-col-left'})
                    right_col = soup.new_tag('div', attrs={'class': 'nav-col nav-col-right'})
                    
                    # Also need to preserve the dividers between links (3 dividers per column)
                    left_dividers = dividers[:3] if len(dividers) >= 3 else dividers
                    # the 4th divider was between link 4 and 5, we can drop it or replace it with the vertical line
                    right_dividers = dividers[4:7] if len(dividers) >= 7 else dividers[-3:]
                    
                    # Append links and dividers to the LEFT column
                    for i in range(len(left_links)):
                        left_col.append(left_links[i])
                        if i < len(left_dividers):
                            left_col.append(left_dividers[i])
                            
                    # Append links and dividers to the RIGHT column
                    for i in range(len(right_links)):
                        right_col.append(right_links[i])
                        if i < len(right_dividers):
                            right_col.append(right_dividers[i])
                            
                    # Clear out nav_right contents
                    nav_right.clear()
                    
                    # Restructure nav_right to wrap the two columns + vertical divider
                    two_col_wrapper = soup.new_tag('div', attrs={'class': 'nav-two-columns'})
                    vertical_divider = soup.new_tag('div', attrs={'class': 'nav-vertical-divider'})
                    
                    two_col_wrapper.append(left_col)
                    two_col_wrapper.append(vertical_divider)
                    two_col_wrapper.append(right_col)
                    
                    nav_right.append(two_col_wrapper)
                    nav_right['style'] = "width: 100%;" # Ensure the container takes full width of the overlay
                    
                    print(f"[{os.path.basename(html_path)}] Successfully restructured sidebar to two columns.")
                else:
                    print(f"[{os.path.basename(html_path)}] Warn: Not enough links found ({len(links)}). Expected >= 8.")
    else:
         print(f"[{os.path.basename(html_path)}] Error: No <div class='nav-grid'> found.")

    # 2. Inject Required CSS
    head = soup.find('head')
    if head:
        # Check if styles exist
        style_tags = head.find_all('style')
        css_injected = False
        nav_styles = """
    .nav-two-columns {
      display: flex;
      flex-direction: row;
      justify-content: space-between;
      width: 100%;
    }
    .nav-col {
      flex: 1;
      display: flex;
      flex-direction: column;
    }
    .nav-vertical-divider {
      width: 1px;
      background-color: rgba(255, 255, 255, 0.4);
      margin: 0 3rem;
    }
    /* Mobile Responsive styling */
    @media (max-width: 767px) {
      .nav-two-columns {
        flex-direction: column;
      }
      .nav-vertical-divider {
        width: 100%;
        height: 1px;
        margin: 1.5rem 0;
      }
    }
"""     
        for style_tag in style_tags:
            if '.nav-two-columns' in style_tag.text:
                css_injected = True
                break
                
        if not css_injected:
            if style_tags:
                # Append to existing
                style_tags[0].append(nav_styles)
            else:
                # Create a new style tag
                new_style = soup.new_tag('style')
                new_style.string = nav_styles
                head.append(new_style)
            print(f"[{os.path.basename(html_path)}] Injected CSS for 2 columns layout.")

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))


if __name__ == '__main__':
    base_dir = '/home/zulpikar/Documents/wbflow/cravia1'
    files_to_update = [
        'index.html',
        'about.html', 
        'security.html',
        'features.html',
        'service.html',
        'work.html',
        'blog.html',
        'contact.html',
        '404.html'
    ]

    for file_name in files_to_update:
        file_path = os.path.join(base_dir, file_name)
        if os.path.exists(file_path):
            update_sidebar_layout(file_path)
        else:
            print(f"File not found: {file_path}")
