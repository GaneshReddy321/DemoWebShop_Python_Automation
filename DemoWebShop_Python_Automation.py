from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.screenshot import take_screenshot
import os
from datetime import datetime



driver = webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com")
driver.maximize_window()
screenshot_dir = r"D:\DemoWebShop_Python_Automation\screenshots"
os.makedirs(screenshot_dir, exist_ok=True)
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

'''emailId ="360ganeshreddy360@gmail.com"
password = "Dattebayoo1@"'''

def Login_Flow(emailId,password):
    wait = WebDriverWait(driver, 10)
    login_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log in")))
    login_button.click()

    email_box = wait.until(EC.visibility_of_element_located((By.ID, "Email")))
    email_box.clear()
    email_box.send_keys(emailId)

    password_box =wait.until(EC.visibility_of_element_located((By.ID, "Password")))
    password_box.clear()
    password_box.send_keys(password)

    screenshot_path = os.path.join(screenshot_dir, f"Login Page{timestamp}.png")
    driver.save_screenshot(screenshot_path)

    enter_button =wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.login-button")))
    enter_button.click()

    screenshot_path = os.path.join(screenshot_dir, f"Home Page{timestamp}.png")
    driver.save_screenshot(screenshot_path)

    user_email_element = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "a.account")))

    actual_email = user_email_element.text

    if actual_email == emailId:

        print(f"✅ LOGIN VERIFIED: {emailId} successfully logged in.")
    else:

        assert False, f"❌ LOGIN FAILED: expected {emailId}, but got {actual_email}"










def buy_Jeans():
    wait = WebDriverWait(driver, 10)

    apperal_Button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Apparel & Shoes")))
    apperal_Button.click()

    BlueJeans_Button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Blue Jeans")))
    BlueJeans_Button.click()

    visible_price = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"price-value-36")))
    price = visible_price.text
    price = float(price)
    print(f"price = {price}" )

    AddToCart_Button = wait.until(EC.visibility_of_element_located((By.ID, "add-to-cart-button-36")))
    AddToCart_Button.click()

def shoppingCart():
    wait = WebDriverWait(driver, 10)
    sub_Total = 0 


    apperal_Button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Shopping cart")))
    apperal_Button.click()

    screenshot_path = os.path.join(screenshot_dir, f"Shopping Cart{timestamp}.png")
    driver.save_screenshot(screenshot_path)

    table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tr.cart-item-row")))
    for row in table:

        product_name = row.find_element(By.CSS_SELECTOR, "td.product").text
        price_text = row.find_element(By.CSS_SELECTOR, "td.unit-price").text
        qty = row.find_element(By.CSS_SELECTOR, "td.qty input").get_attribute("value")
        total_text = row.find_element(By.CSS_SELECTOR, "td.subtotal .product-subtotal").text

        price_text = float(price_text)
        qty = int(qty)
        total_text = float(total_text)
        sub_Total = sub_Total + total_text
        sub_Total = int(sub_Total)



        print(f"Product Name and Details : {product_name} \n  Price : {price_text} \n Quantity : {qty} \n Total :{total_text}")
       # print(product_name, price_text, qty, total_text)

    actual_SubTotal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "table.cart-total span.product-price"))).text
    actual_SubTotal = int(float(actual_SubTotal))



    if actual_SubTotal == sub_Total:
        print("Verification Done , Actual SubTotal = SubTotal")
    else :
        print(f"Verification Failed {actual_SubTotal} {sub_Total}")  

    checkBox = wait.until(EC.visibility_of_element_located((By.ID, "termsofservice")))
    checkBox.click()

    Checkout_Button = wait.until(EC.visibility_of_element_located((By.ID, "checkout")))
    Checkout_Button.click()

def checkout():
    
    wait = WebDriverWait(driver, 10)

    address_Button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#billing-buttons-container input.new-address-next-step-button")))
    address_Button.click()

    Shipping_Address_Button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#shipping-buttons-container input.new-address-next-step-button")))
    Shipping_Address_Button.click()

    Shipping_Method_Option = wait.until(EC.visibility_of_element_located((By.ID, "shippingoption_0")))
    Shipping_Method_Option.click()

    Shipping_Method_Button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#shipping-method-buttons-container input.shipping-method-next-step-button")))
    Shipping_Method_Button.click()

    Payment_Method_Button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#payment-method-buttons-container input.payment-method-next-step-button")))
    Payment_Method_Button.click()

    Payment_Info_Button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#payment-info-buttons-container input.payment-info-next-step-button")))
    Payment_Info_Button.click()

    totals_table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.totals table.cart-total")))
    subtotal = totals_table.find_element(By.XPATH,".//td[@class='cart-total-left' and contains(.,'Sub-Total')]/following-sibling::td//span[@class='product-price']").text
    print(f"subtotal : {subtotal}")

    ConfrimOrder_Button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#confirm-order-buttons-container input.confirm-order-next-step-button")))
    ConfrimOrder_Button.click()
    
def Final_Page():
    wait = WebDriverWait(driver, 10)


   # wait.until(EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(),'successfully')]")))
    Order_Number = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.section.order-completed ul.details li"))).text
    Order_Number = Order_Number.split(":")[1].strip()

    screenshot_path = os.path.join(screenshot_dir, f"Order Number{timestamp}.png")
    driver.save_screenshot(screenshot_path)

    print(f"Order Number : {Order_Number}")

    Conitnue_Button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.section.order-completed input.order-completed-continue-button")))
    Conitnue_Button.click()


def practice():
    price = "1.00"
    

    price = float(price)
    print(price*6)



Login_Flow("360ganeshreddy360@gmail.com","Dattebayoo1@")
buy_Jeans()
shoppingCart()
checkout()
Final_Page()

#practice()

#input("Press ENTER to close browser...")
driver.quit()