# ERP Barcode Scanning System

A modern, intuitive ERP barcode scanning warehouse management system built with FastAPI and SQLite.

## Features

- **Barcode Scanning**: Real-time barcode scanning using camera or file upload
- **Product Management**: Add, edit, delete, and import products with bulk operations
- **Stock Query**: View current stock levels and product information
- **Statistics & Analysis**: Visual dashboards with trend charts, category analysis, operator performance, and top products
- **Backup Management**: Manual and automated database backups with restore functionality
- **Offline Support**: Continue working offline with data synchronization when online
- **Responsive Design**: Modern UI that works on desktop and mobile devices

## Technologies Used

- **Backend**: FastAPI (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Barcode Scanning**: Quagga.js
- **Data Visualization**: Chart.js
- **Styling**: CSS Custom Properties (Variables) for theming

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/zhu4388501/ERP-Barcode-Scanning-Warehouse-Management.git
   cd ERP-Barcode-Scanning-Warehouse-Management
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python -m uvicorn app:app --reload
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

## Project Structure

```
.
├── app.py              # Main FastAPI application
├── main.py             # Entry point for running the server
├── requirements.txt    # Project dependencies
├── .gitignore          # Git ignore file
├── models/             # Database models
├── routes/             # API routes
├── schemas/            # Pydantic models for request/response
├── static/             # Static files (CSS, JavaScript)
└── utils/              # Utility functions
```

## API Endpoints

- **Barcode Scanning**: `/api/scan/`
- **Product Management**: `/api/product/`
- **Stock Query**: `/api/stock/`
- **Statistics**: `/api/statistics/`
- **Backup**: `/api/backup/`
- **Offline**: `/api/offline/`

## Database

The application uses SQLite as its database (erp_scan.db). This provides a lightweight, file-based database solution that's easy to deploy and maintain.

## Security

- CORS configured for controlled access
- Input validation using Pydantic models
- SQL injection protection through SQLAlchemy ORM

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License