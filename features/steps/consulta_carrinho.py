from behave import given, when, then

base_url = 'https://www.amazon.com.br/gp/product/8595084378/ref=ox_sc_act_title_2?smid=A1ZZFT5FULY4LN&psc=1'

element_add_to_cart = 'add-to-cart-button'
element_cart = 'nav-cart'
cart_item = 'sc-product-title'


@given(u'acesso a pagina de um produto na Amazon')
def step_impl(context):
    context.web.get(base_url)

@when(u'clico no adicionar o produto ao carrinho')
def step_impl(context):
    context.element_cart = context.web.find_element('id', element_add_to_cart)
    context.element_cart.click()
    context.web.implicitly_wait(3)

    context.element_cart = context.web.find_element('id', element_cart)
    context.element_cart.click()
    context.web.implicitly_wait(3)

@when(u'carrinho e exibido')
def step_impl(context):
    context.cart_item = context.web.find_element('class name', cart_item)

@then(u'devo saber quais itens estao no carrinho')
def step_impl(context):
    item = context.cart_item.text
    print('\n' + item)    

    file = open("features/results/results.txt", 'a')
    file.write(item)
