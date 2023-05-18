import os


naming_dict = {
    "01. sales": "01. Sales",
    "02. architect": "02. Architect",
    "03. IT": "03. Information Technology (IT)",
    "04. Law": "04. Law",
    "05. Engineer": "05. Engineer",
    "06. Creator": "06. Creator",
    "07. marketing": "07. Marketing",
    "08. Police": "08. Police",
    "09. Delivery": "09. Delivery",
    "10. Mechanic": "10. Mechanic",
    "11. Construction": "11. Construction",
    "12. writer": "12. Writer",
    "13. Media": "13. Media",
    "14. HR": "14. Human Resources (HR)",
    "15. buy": "15. Buyer",
    "16. maid": "16. Maid",
    "17. Hotel": "17. Hotel/Hospitality",
    "18. Call center": "18. Call Center",
    "19. Telecom": "19. Telecommunications",
    "20. Ticket": "20. Ticketing",
    "21. Banking": "21. Banking",
    "22. Secretary": "22. Secretary/Administrative Assistant",
    "23. Management": "23. Management",
    "24. Economics": "24. Economics",
    "25. Medical": "25. Medical/Healthcare",
    "26. Driver": "26. Driver",
    "27. Manager": "27. Manager",
    "28. Clothing": "28. Clothing/Fashion",
    "29. Finance": "29. Finance/Financial Services",
    "31. Insurance": "31. Insurance",
    "32. Food": "32. Food/Culinary",
    "33. Government": "33. Government",
    "34. Part Time": "34. Part-time",
    "35. Science": "35. Science",
    "36. Translator": "36. Translator/Interpreter",
    "37. Manufacturing": "37. Manufacturing",
    "38. Geology": "38. Geology/Earth Sciences",
    "39. Health": "39. Health/Wellness",
    "40. Geography": "40. Geography",
    "41. Property": "41. Property/Real Estate",
    "43. Graphics": "43. Graphics/Design",
    "44. Business Development": "44. Business Development",
    "45. Education": "45. Education",
    "46. Mall": "46. Mall/Retail",
    "47. E-commerce": "47. E-commerce",
    "49. Others": "49. Others"
}

folder_path = "./test"

for subfolder in os.listdir(folder_path):
    subfolder_path = os.path.join(folder_path, subfolder)

    if os.path.isdir(subfolder_path):
        new_subfolder_name = naming_dict.get(subfolder, subfolder)
        new_subfolder_path = os.path.join(folder_path, new_subfolder_name)
        try:
            os.rename(subfolder_path, new_subfolder_path)
            print(f"Renamed {subfolder_path} to {new_subfolder_path}")
        except PermissionError:
            print(f"Could not rename {subfolder_path} due to a PermissionError")
            continue