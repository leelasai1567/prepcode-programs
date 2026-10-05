total_products=157
products_per_box=12
complete_boxes=total_products//products_per_box
remaining_products=total_products%products_per_box
print(f"complete_boxes:{complete_boxes}")
print(f"remaining_products:{remaining_products}")