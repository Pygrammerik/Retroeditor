from PIL import Image, ImageDraw

def create_icon():
    # Создаем изображение 256x256 пикселей
    size = 256
    image = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    
    # Рисуем фон (квадрат с закругленными углами)
    margin = 20
    draw.rounded_rectangle(
        [(margin, margin), (size-margin, size-margin)],
        radius=30,
        fill='#2c3e50'  # Тёмно-синий цвет для ретро-стиля
    )
    
    # Рисуем основную часть пишущей машинки
    typewriter_margin = 40
    draw.rectangle(
        [(typewriter_margin, typewriter_margin), 
         (size-typewriter_margin, size-typewriter_margin)],
        fill='#34495e'  # Чуть светлее для объема
    )
    
    # Рисуем клавиши
    key_size = 25
    key_spacing = 5
    start_x = typewriter_margin + 30
    start_y = typewriter_margin + 40
    
    # Рисуем три ряда клавиш
    for row in range(3):
        for col in range(4):
            x = start_x + col * (key_size + key_spacing)
            y = start_y + row * (key_size + key_spacing)
            # Рисуем клавишу
            draw.rectangle(
                [(x, y), (x + key_size, y + key_size)],
                fill='#ecf0f1',  # Светло-серый для клавиш
                outline='#2c3e50'
            )
            # Рисуем символ на клавише
            draw.rectangle(
                [(x + 5, y + 5), (x + key_size - 5, y + key_size - 5)],
                fill='#95a5a6'  # Тёмно-серый для символов
            )
    
    # Рисуем бумагу
    paper_margin = 30
    draw.rectangle(
        [(paper_margin, paper_margin), 
         (size-paper_margin, size-paper_margin)],
        fill='#f5f6fa',  # Светлый цвет для бумаги
        outline='#2c3e50'
    )
    
    # Рисуем линии текста на бумаге
    line_spacing = 15
    line_width = 120
    start_y = paper_margin + 40
    for i in range(4):
        y = start_y + i * line_spacing
        draw.rectangle(
            [(paper_margin + 20, y), 
             (paper_margin + 20 + line_width, y + 4)],
            fill='#bdc3c7'  # Серый цвет для текста
        )
    
    # Сохраняем как .ico
    image.save('retro_editor.ico', format='ICO', sizes=[(256, 256)])

if __name__ == '__main__':
    create_icon() 