# Multiple_Image_Upload - Django App

Multiple_Image_Upload is a Django web application that allows users to save multiple images in a single text field and perform various operations like update, delete, and extend the data. The app is named "multipleimagesapp" within the project.

## Features

- Upload and save multiple images in a single text field.
- Update the title.
- Delete images.
- View and extend the gallery by adding more images.

## Requirements

- Python (>= 3.6)
- Django (>= 2.2)

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/your-username/Multiple_Image_Upload.git
cd Multiple_Image_Upload
```
### 1. Install the dependencies:
```bash
pip install -r requirements.txt
```
### 2. Run the development server:
```bash
python manage.py runserver
```

### 3. Open your web browser and visit http://localhost:8000/ to access the app.
## Usage
1. On the homepage, you'll see a form to upload images along with a title for your gallery.
2. Choose one or multiple images and give a title to your gallery, then click "Upload Images."
3. The images and their associated data will be saved in the database and displayed in a table.
4. To update the image, click on the "Update" button next to the image's.
5. To delete an image and its data, click on the "Delete" link next to the image's row in the table.
6. To add more images to an existing gallery, click on the "Upload Images" button in the "Upload" column.
7. The new images will be added to the existing gallery, and all data will be stored in the database.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


