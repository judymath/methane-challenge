import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Image Prediction", page_icon="📈")

st.markdown("# Image Prediction")
st.sidebar.header("Methane Detection mockup")
st.write(
    """
    
    This mockup illustrates how lab5 is detecting methane plume by satellite image.

    Try to upload one image and see the magic. 🪄 ✨
    
    """
)

file_up = st.file_uploader("", type=["jpg", "jpeg", "png","tif", "tiff"], accept_multiple_files=True)

block_content = ""

if file_up:

    # Generate a random likelihood score for methane plume presence
    likelihood = np.random.normal(0.7, 0.1)

    # Clamp the value between 0 and 1 for valid probability representation
    likelihood = max(0, min(1, likelihood))
    # Display the result in a larger, emphasized format
    # Set the block content with the likelihood score
    block_content = f"The likelihood of a methane plume in this location is: <span style='color: red;'>{likelihood:.2%}</span>"

# Display the result block
st.markdown(
    f"<div style='background-color: #000; padding: 10px; border-radius: 5px;'>"
    f"<p style='color: #fff;'>Prediction Result</p>"  # Using <h3> for a slightly smaller title
    f"<p style='color: #fff;'>{block_content}</p>"
    f"</div>", 
    unsafe_allow_html=True
)
art = r"""
Charizard is producing methane today and our satellite captured some images for us.

                 ."-,.__
                 `.     `.  ,
              .--'  .._,'"-' `.
             .    .'         `'
             `.   /          ,'
               `  '--.   ,-"'
                `"`   |  \
                   -. \, |
                    `--Y.'      ___.
                         \     L._, \
               _.,        `.   <  <\                _
             ,' '           `, `.   | \            ( `
          ../, `.            `  |    .\`.           \ \_
         ,' ,..  .           _.,'    ||\l            )  '".
        , ,'   \           ,'.-.`-._,'  |           .  _._`.
      ,' /      \ \        `' ' `--/   | \          / /   ..\
    .'  /        \ .         |\__ - _ ,'` `        / /     `.`.
    |  '          ..         `-...-"  |  `-'      / /        . `.
    | /           |L__           |    |          / /          `. `.
   , /            .   .          |    |         / /             ` `
  / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \
 / .           \"`_/. `-_ \_,.  ,'    +-' `-'  _,        ..,-.    \`.
.  '         .-f    ,'   `    '.       \__.---'     _   .'   '     \ \
' /          `.'    l     .' /          \..      ,_|/   `.  ,'`     L`
|'      _.-""` `.    \ _,'  `            \ `.___`.'"`-.  , |   |    | \
||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|
||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||
|| '              V      / /           `   | `   ,'   ,' '.    !  `. ||
||/            _,-------7 '              . |  `-'    l         /    `||
. |          ,' .-   ,' ||               | .-.        `.      .'     ||
 `'        ,'    `".'    |               |    `.        '. -.'       `'
          /      ,'      |               |,'    \-.._,.'/'
          .     /        .               .       \    .''
        .`.    |         `.             /         :_,'.'
          \ `...\   _     ,'-.        .'         /_.-'
           `-.__ `,  `'   .  _.>----''.  _  __  /
                .'        /"'          |  "'   '_
               /_|.-'\ ,".             '.'`__'-( \
                 / ,"'"\,'               `/  `-.|" mh

"""
st.divider()
st.text(art)