from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QFormLayout,
    QStatusBar,
    QHeaderView,
    QScrollArea,
    QFrame,
    QSizePolicy,
)
from PySide6.QtGui import QPalette, QColor, QFont, QDoubleValidator, QIntValidator
from PySide6.QtCore import Qt, Signal

from models import Inventory
from inventory_service import InventoryService


class KpiCard(QFrame):
    def __init__(self, title: str, value: str = "-", color: str = "#4a90d9"):
        super().__init__()
        self.setFrameShape(QFrame.StyledPanel)
        self.setFixedSize(180, 80)
        self.setStyleSheet(
            f"""
            QFrame {{
                background-color: #2c2c2c;
                border: 1px solid {color};
                border-radius: 8px;
            }}
            """
        )
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 8, 10, 8)

        self._title = QLabel(title)
        self._title.setStyleSheet("color: #aaaaaa; font-size: 11px;")
        self._title.setAlignment(Qt.AlignCenter)

        self._value = QLabel(value)
        self._value.setStyleSheet(
            f"color: {color}; font-size: 20px; font-weight: bold;"
        )
        self._value.setAlignment(Qt.AlignCenter)

        layout.addWidget(self._title)
        layout.addWidget(self._value)

    def update_value(self, value: str):
        self._value.setText(value)


class InventoryApp(QMainWindow):
    logout_requested = Signal()

    def __init__(self, username: str | None = None, role: str = "viewer"):
        super().__init__()
        self.inventory = Inventory()
        self.service = InventoryService(self.inventory)
        self.role = role

        self.chart_canvas: FigureCanvas | None = None
        self.chart_figure: Figure | None = None
        self.chart_placeholder: QLabel | None = None

        self.setWindowTitle("📦 Inventory Management System")
        self.resize(1100, 750)
        self._apply_dark_theme()

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        central = QWidget()
        self.setCentralWidget(central)
        root = QVBoxLayout(central)
        root.setContentsMargins(10, 10, 10, 10)

        # Top bar
        top_bar = QHBoxLayout()
        if username:
            lbl = QLabel(f"👤  {username}  |  Role: {role.upper()}")
            lbl.setStyleSheet("color: #64b5f6; font-size: 13px; font-weight: bold;")
            top_bar.addWidget(lbl)
        top_bar.addStretch()

        logout_btn = QPushButton("🚪 Logout")
        logout_btn.setStyleSheet(
            "background:#c0392b; color:white; padding:4px 12px; border-radius:4px;"
        )
        logout_btn.clicked.connect(self.logout_requested.emit)
        top_bar.addWidget(logout_btn)
        root.addLayout(top_bar)

        # Tabs
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet(
            """
            QTabBar::tab          { padding: 8px 20px; font-size: 13px; }
            QTabBar::tab:selected { background: #3a3a3a; color: #64b5f6; }
            """
        )
        root.addWidget(self.tabs)

        self._build_menu_tab()
        if role == "admin":
            self._build_product_tab()
        self._build_dashboard_tab()

    def _apply_dark_theme(self):
        palette = QPalette()
        for role, color in {
            QPalette.Window: QColor(28, 28, 28),
            QPalette.WindowText: QColor(220, 220, 220),
            QPalette.Base: QColor(22, 22, 22),
            QPalette.AlternateBase: QColor(35, 35, 35),
            QPalette.Text: QColor(220, 220, 220),
            QPalette.Button: QColor(55, 55, 55),
            QPalette.ButtonText: QColor(220, 220, 220),
            QPalette.Highlight: QColor(100, 150, 200),
            QPalette.HighlightedText: QColor(255, 255, 255),
        }.items():
            palette.setColor(role, color)
        self.setPalette(palette)

    def _build_menu_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("📦 Inventory Management System")
        title.setFont(QFont("Arial", 22, QFont.Bold))
        title.setStyleSheet("color: #64b5f6;")
        title.setAlignment(Qt.AlignCenter)

        sub = QLabel("Use the tabs above to manage products and view the dashboard.")
        sub.setStyleSheet("color: #aaaaaa; font-size: 13px;")
        sub.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)
        layout.addSpacing(10)
        layout.addWidget(sub)
        self.tabs.addTab(tab, "🏠 Menu")

    def _build_product_tab(self):
        tab = QWidget()
        outer = QVBoxLayout(tab)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        content = QWidget()
        form = QFormLayout(content)
        form.setLabelAlignment(Qt.AlignRight)
        form.setSpacing(12)
        form.setContentsMargins(40, 20, 40, 20)

        def _entry(placeholder: str = "") -> QLineEdit:
            e = QLineEdit()
            e.setPlaceholderText(placeholder)
            e.setStyleSheet(
                "background:#2a2a2a; color:#ddd; border:1px solid #555;"
                "border-radius:4px; padding:5px;"
            )
            return e

        self.entry_id = _entry("e.g. P001")
        self.entry_name = _entry("e.g. Apple")
        self.entry_price = _entry("e.g. 9.99")
        self.entry_qty = _entry("e.g. 50")
        self.entry_cat = _entry("e.g. Fruit")

        self.entry_price.setValidator(QDoubleValidator(0.0, 1_000_000_000.0, 2, self))
        self.entry_qty.setValidator(QIntValidator(0, 1_000_000_000, self))

        for label, widget in [
            ("Item ID:", self.entry_id),
            ("Name:", self.entry_name),
            ("Price:", self.entry_price),
            ("Quantity:", self.entry_qty),
            ("Category:", self.entry_cat),
        ]:
            form.addRow(label, widget)

        btn_row = QHBoxLayout()

        self.btn_add = QPushButton("➕  Add")
        self.btn_add.setStyleSheet(
            "background:#27ae60; color:white; padding:8px 18px;"
            "border-radius:5px; font-size:13px;"
        )
        self.btn_add.clicked.connect(self.add_product)
        btn_row.addWidget(self.btn_add)

        btn_remove = QPushButton("🗑  Remove")
        btn_remove.setStyleSheet(
            "background:#c0392b; color:white; padding:8px 18px;"
            "border-radius:5px; font-size:13px;"
        )
        btn_remove.clicked.connect(self.remove_product)
        btn_row.addWidget(btn_remove)

        self.btn_update = QPushButton("✏️  Update")
        self.btn_update.setStyleSheet(
            "background:#2980b9; color:white; padding:8px 18px;"
            "border-radius:5px; font-size:13px;"
        )
        self.btn_update.clicked.connect(self.update_product)
        btn_row.addWidget(self.btn_update)

        btn_clear = QPushButton("🧹  Clear")
        btn_clear.setStyleSheet(
            "background:#555555; color:white; padding:8px 18px;"
            "border-radius:5px; font-size:13px;"
        )
        btn_clear.clicked.connect(self._clear_entries)
        btn_row.addWidget(btn_clear)

        form.addRow(btn_row)

        scroll.setWidget(content)
        outer.addWidget(scroll)

        self._bind_validation_signals()
        self._validate_form()

        self.tabs.addTab(tab, "🛠 Product Info")

    def _build_dashboard_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Price", "Qty", "Category"])
        self.table.setAlternatingRowColors(True)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSortingEnabled(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setStyleSheet("font-size: 13px;")
        layout.addWidget(self.table, stretch=3)

        kpi_row = QHBoxLayout()
        kpi_row.setAlignment(Qt.AlignCenter)
        self.kpi_total_qty = KpiCard("Total Quantity", "-", "#64b5f6")
        self.kpi_low_stock = KpiCard("Low Stock (<10)", "-", "#e74c3c")
        self.kpi_avg_price = KpiCard("Avg Price", "-", "#2ecc71")
        self.kpi_cat_count = KpiCard("Categories", "-", "#f39c12")
        for card in [
            self.kpi_total_qty,
            self.kpi_low_stock,
            self.kpi_avg_price,
            self.kpi_cat_count,
        ]:
            kpi_row.addWidget(card)
        layout.addLayout(kpi_row)

        self.chart_frame = QWidget()
        self.chart_frame.setMinimumHeight(280)
        self.chart_frame.setLayout(QVBoxLayout())
        self.chart_frame.layout().setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.chart_frame, stretch=2)

        btn_row = QHBoxLayout()
        for text, color, slot in [
            ("📋  List Products", "#2980b9", self.list_products),
            ("📊  Update Dashboard", "#8e44ad", self.update_dashboard),
        ]:
            btn = QPushButton(text)
            btn.setStyleSheet(
                f"background:{color}; color:white; padding:8px 22px;"
                "border-radius:5px; font-size:13px;"
            )
            btn.clicked.connect(slot)
            btn_row.addWidget(btn)
        layout.addLayout(btn_row)

        self.tabs.addTab(tab, "📊 Data Dashboard")

    def _bind_validation_signals(self):
        for e in [
            self.entry_id,
            self.entry_name,
            self.entry_price,
            self.entry_qty,
            self.entry_cat,
        ]:
            e.textChanged.connect(self._validate_form)

    def _validate_form(self):
        item_id = self.entry_id.text().strip()
        name = self.entry_name.text().strip()
        price = self.entry_price.text().strip()
        qty = self.entry_qty.text().strip()
        cat = self.entry_cat.text().strip()

        add_valid = all([item_id, name, price, qty, cat])
        update_valid = bool(item_id and (price or qty))

        self.btn_add.setEnabled(add_valid)
        self.btn_update.setEnabled(update_valid)

    def _clear_entries(self):
        for e in [
            self.entry_id,
            self.entry_name,
            self.entry_price,
            self.entry_qty,
            self.entry_cat,
        ]:
            e.clear()
        self._validate_form()

    def _status(self, msg: str, ms: int = 3000):
        self.status_bar.showMessage(msg, ms)

    def _refresh_product_views(self):
        self.list_products()
        self.update_dashboard()

    def add_product(self):
        result = self.service.add_product(
            self.entry_id.text(),
            self.entry_name.text(),
            self.entry_price.text(),
            self.entry_qty.text(),
            self.entry_cat.text(),
        )
        if result.ok:
            self._status(f"✅ {result.message}")
            self._clear_entries()
            self._refresh_product_views()
        else:
            QMessageBox.warning(self, "Cannot Add Product", result.message)

    def remove_product(self):
        item_id = self.entry_id.text().strip()
        if not item_id:
            QMessageBox.warning(self, "Missing ID", "Please enter an Item ID.")
            return

        confirm = QMessageBox.question(
            self,
            "Confirm Remove",
            f"Remove product '{item_id}'?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if confirm != QMessageBox.Yes:
            return

        result = self.service.remove_product(item_id)
        if result.ok:
            self._status(f"🗑 {result.message}")
            self._clear_entries()
            self._refresh_product_views()
        else:
            QMessageBox.critical(self, "Cannot Remove Product", result.message)

    def update_product(self):
        result = self.service.update_product(
            self.entry_id.text(),
            self.entry_price.text(),
            self.entry_qty.text(),
        )
        if result.ok:
            self._status(f"✏️ {result.message}")
            self._refresh_product_views()
        else:
            QMessageBox.warning(self, "Cannot Update Product", result.message)

    def list_products(self):
        self.table.setSortingEnabled(False)
        products = list(self.inventory.products.values())
        self.table.setRowCount(len(products))

        for row, p in enumerate(products):
            self.table.setItem(row, 0, QTableWidgetItem(p.item_id))
            self.table.setItem(row, 1, QTableWidgetItem(p.name))

            price_item = QTableWidgetItem()
            price_item.setData(Qt.DisplayRole, p.price)
            self.table.setItem(row, 2, price_item)

            qty_item = QTableWidgetItem()
            qty_item.setData(Qt.DisplayRole, p.get_quantity())
            self.table.setItem(row, 3, qty_item)

            self.table.setItem(row, 4, QTableWidgetItem(p.category))

        self.table.setSortingEnabled(True)

    def _clear_chart_widgets(self):
        layout = self.chart_frame.layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
                widget.deleteLater()

        self.chart_canvas = None
        self.chart_figure = None
        self.chart_placeholder = None

    def update_dashboard(self):
        self._clear_chart_widgets()

        summary = self.inventory.category_summary()
        if summary:
            fig = Figure(figsize=(5, 3.5), facecolor="#1c1c1c")
            self.chart_figure = fig

            ax = fig.add_subplot(111)
            ax.set_facecolor("#1c1c1c")
            ax.pie(
                summary.values(),
                labels=summary.keys(),
                autopct="%1.1f%%",
                startangle=90,
                textprops={"color": "#dddddd", "fontsize": 10},
            )
            ax.set_title("Inventory by Category", color="#64b5f6", fontsize=13, pad=10)
            fig.tight_layout()

            self.chart_canvas = FigureCanvas(fig)
            self.chart_canvas.setSizePolicy(
                QSizePolicy.Expanding, QSizePolicy.Expanding
            )
            self.chart_frame.layout().addWidget(self.chart_canvas)
        else:
            self.chart_placeholder = QLabel("No data yet. Add products to view chart.")
            self.chart_placeholder.setAlignment(Qt.AlignCenter)
            self.chart_placeholder.setStyleSheet("color:#888; font-size:12px;")
            self.chart_frame.layout().addWidget(self.chart_placeholder)

        self.kpi_total_qty.update_value(str(self.inventory.total_quantity()))
        self.kpi_low_stock.update_value(str(self.inventory.low_stock_count()))
        self.kpi_avg_price.update_value(f"${self.inventory.avg_price():.2f}")
        self.kpi_cat_count.update_value(str(self.inventory.category_count()))
