import os
import shutil

def split_images(source_folder, output_folder, interval=3):
    """
    Разделяет изображения в папке на папки с интервалом.

    Args:
        source_folder: Путь к папке с изображениями.
        output_folder: Путь к папке, куда будут вынесены изображения.
        interval: Интервал, через который выносить изображения (например, 3 = каждая третья).
    """

    # Создаем папку для вывода, если ее нет
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Итерируем по всем папкам в исходной папке
    for subfolder in os.listdir(source_folder):
        subfolder_path = os.path.join(source_folder, subfolder)
        # Проверяем, является ли подпапка директорией
        if os.path.isdir(subfolder_path):
            # Создаем новую папку для вывода
            output_subfolder = os.path.join(output_folder, subfolder)
            if not os.path.exists(output_subfolder):
                os.makedirs(output_subfolder)
            # Сортируем список изображений по имени
            image_files = sorted(os.listdir(subfolder_path))
            # Выносим изображения с заданным интервалом
            for i, image_file in enumerate(image_files):
                if (i + 1) % interval == 0:
                    source_image = os.path.join(subfolder_path, image_file)
                    destination_image = os.path.join(output_subfolder, image_file)
                    shutil.move(source_image, destination_image)

# Пример использования
source_folder = "/Users/mihailprozorskij/Desktop/datasetTest"
output_folder = "/Users/mihailprozorskij/Desktop/new"
interval = 3  # Выносить каждую третью картинку

split_images(source_folder, output_folder, interval)