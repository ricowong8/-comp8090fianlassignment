from dataclasses import dataclass
from typing import Optional

from models import Inventory, Product


@dataclass
class ServiceResult:
    ok: bool
    message: str
    code: str = "ok"


class InventoryService:
    def __init__(self, inventory: Inventory):
        self.inventory = inventory

    def add_product(
        self, item_id: str, name: str, price_text: str, qty_text: str, category: str
    ) -> ServiceResult:
        item_id = item_id.strip()
        name = name.strip()
        category = category.strip()
        price_text = price_text.strip()
        qty_text = qty_text.strip()

        # Required fields
        if not item_id:
            return ServiceResult(False, "Item ID is required.", "missing_item_id")
        if not name:
            return ServiceResult(False, "Name is required.", "missing_name")
        if not category:
            return ServiceResult(False, "Category is required.", "missing_category")
        if not price_text:
            return ServiceResult(False, "Price is required.", "missing_price")
        if not qty_text:
            return ServiceResult(False, "Quantity is required.", "missing_quantity")

        # Parse numeric fields
        try:
            price = float(price_text)
        except ValueError:
            return ServiceResult(
                False, "Price must be a valid number.", "invalid_price"
            )

        try:
            qty = int(qty_text)
        except ValueError:
            return ServiceResult(
                False, "Quantity must be an integer.", "invalid_quantity"
            )

        if price < 0:
            return ServiceResult(False, "Price cannot be negative.", "negative_price")
        if qty < 0:
            return ServiceResult(
                False, "Quantity cannot be negative.", "negative_quantity"
            )

        p = Product(item_id, name, price, qty, category)
        if not self.inventory.add_product(p):
            return ServiceResult(
                False,
                f"Product ID '{item_id}' already exists.",
                "duplicate_item_id",
            )

        return ServiceResult(True, f"'{name}' added successfully.", "added")

    def remove_product(self, item_id: str) -> ServiceResult:
        item_id = item_id.strip()
        if not item_id:
            return ServiceResult(False, "Please enter an Item ID.", "missing_item_id")

        if not self.inventory.remove_product(item_id):
            return ServiceResult(
                False, f"Product '{item_id}' does not exist.", "not_found"
            )

        return ServiceResult(True, f"'{item_id}' removed.", "removed")

    def update_product(
        self, item_id: str, price_text: str, qty_text: str
    ) -> ServiceResult:
        item_id = item_id.strip()
        price_text = price_text.strip()
        qty_text = qty_text.strip()

        if not item_id:
            return ServiceResult(False, "Item ID is required.", "missing_item_id")

        if not price_text and not qty_text:
            return ServiceResult(
                False,
                "Please provide at least one value to update (Price or Quantity).",
                "nothing_to_update",
            )

        new_price: Optional[float] = None
        new_qty: Optional[int] = None

        if price_text:
            try:
                new_price = float(price_text)
            except ValueError:
                return ServiceResult(
                    False, "Price must be a valid number.", "invalid_price"
                )
            if new_price < 0:
                return ServiceResult(
                    False, "Price cannot be negative.", "negative_price"
                )

        if qty_text:
            try:
                new_qty = int(qty_text)
            except ValueError:
                return ServiceResult(
                    False, "Quantity must be an integer.", "invalid_quantity"
                )
            if new_qty < 0:
                return ServiceResult(
                    False, "Quantity cannot be negative.", "negative_quantity"
                )

        if not self.inventory.update_product(item_id, new_price, new_qty):
            return ServiceResult(
                False, f"Product '{item_id}' does not exist.", "not_found"
            )

        return ServiceResult(True, f"'{item_id}' updated.", "updated")
