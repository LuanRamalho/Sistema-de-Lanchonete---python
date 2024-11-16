import tkinter as tk
from tkinter import ttk

def calculate_total():
    """Calcula o preço total com base nas quantidades e exibe os valores individuais."""
    total = 0
    result_text.delete(1.0, tk.END)  # Limpa os resultados anteriores
    for var, entry, price, item in zip(checkbox_vars, quantity_entries, prices, items):
        if var.get():
            try:
                quantity = int(entry.get())
                if quantity < 0:
                    quantity = 0
                    entry.delete(0, tk.END)
                    entry.insert(0, "0")
            except ValueError:
                quantity = 0
            item_total = quantity * price
            result_text.insert(tk.END, f"{item[0]} (x{quantity}): R${item_total:.2f}\n")
            total += item_total
    total_label.config(text=f"R${total:.2f}")
    calculate_change()

def calculate_change():
    """Calcula o troco com base no valor pago."""
    try:
        total = float(total_label.cget("text")[2:])
        payment = float(payment_entry.get())
        change = payment - total
        if change < 0:
            change_label.config(text="Valor insuficiente!")
        else:
            change_label.config(text=f"R${change:.2f}")
    except ValueError:
        change_label.config(text="R$0.00")

# Configuração da janela principal
root = tk.Tk()
root.title("Sistema de Lanchonete")
root.geometry("600x800")
root.configure(bg="#f4f4f4")

# Adicionando um canvas para permitir rolagem
main_canvas = tk.Canvas(root, bg="#f4f4f4")
main_canvas.pack(side="left", fill="both", expand=True)

main_scrollbar = ttk.Scrollbar(root, orient="vertical", command=main_canvas.yview)
main_scrollbar.pack(side="right", fill="y")

main_frame = tk.Frame(main_canvas, bg="#f4f4f4")
main_canvas.create_window((0, 0), window=main_frame, anchor="nw")
main_canvas.configure(yscrollcommand=main_scrollbar.set)

def configure_canvas(event):
    main_canvas.configure(scrollregion=main_canvas.bbox("all"))

main_frame.bind("<Configure>", configure_canvas)

# Cabeçalho
header = tk.Label(main_frame, text="Sistema de Lanchonete", font=("Arial", 24, "bold"), bg="#6200ea", fg="white")
header.pack(fill="x", pady=20)

subheader = tk.Label(main_frame, text="Escolha seus itens e quantidades", font=("Arial", 16), bg="#f4f4f4", fg="#6200ea")
subheader.pack(pady=10)

# Itens e preços
items = [
    ("Cachorro-Quente", 5.00),
    ("Hambúrguer", 5.00),
    ("Batata-Frita", 2.50),
    ("Pizza", 2.00),
    ("Pastel", 2.00),
    ("Empada", 2.50),
    ("Salgado", 2.50),
    ("Refrigerante", 1.00),
    ("Suco", 1.50),
    ("Refresco", 1.00)
]

prices = [item[1] for item in items]
checkbox_vars = []
quantity_entries = []

# Criação dos checkboxes e caixas de quantidade
for item, price in items:
    var = tk.BooleanVar()
    checkbox_vars.append(var)
    frame = tk.Frame(main_frame, bg="#fff")
    frame.pack(fill="x", padx=20, pady=5)
    
    checkbox = tk.Checkbutton(
        frame,
        text=f"{item} - R${price:.2f}",
        variable=var,
        font=("Arial", 12),
        bg="#fff",
        fg="#555",
        anchor="w",
        activebackground="#f4f4f4",
        command=calculate_total
    )
    checkbox.pack(side="left")
    
    quantity_entry = tk.Entry(frame, width=5, font=("Arial", 12), justify="center", fg="#333")
    quantity_entry.insert(0, "0")
    quantity_entry.pack(side="right", padx=10)
    quantity_entries.append(quantity_entry)

# Exibição do total
total_frame = tk.Frame(main_frame, bg="#f4f4f4")
total_frame.pack(pady=10)

total_label_text = tk.Label(total_frame, text="Total: ", font=("Arial", 14), bg="#f4f4f4", fg="#6200ea")
total_label_text.pack(side="left")

total_label = tk.Label(total_frame, text="R$0.00", font=("Arial", 14, "bold"), bg="#f4f4f4", fg="#28a745")
total_label.pack(side="left")

# Resultado dos cálculos individuais
result_frame = tk.Frame(main_frame, bg="#f4f4f4")
result_frame.pack(pady=10, padx=20, fill="both", expand=True)

result_scrollbar = ttk.Scrollbar(result_frame, orient="vertical")
result_scrollbar.pack(side="right", fill="y")

result_text = tk.Text(result_frame, height=10, font=("Arial", 12), bg="#e8f5e9", fg="#333", yscrollcommand=result_scrollbar.set)
result_text.pack(side="left", fill="both", expand=True)

result_scrollbar.config(command=result_text.yview)

# Entrada do pagamento
payment_entry = tk.Entry(main_frame, font=("Arial", 14), justify="center", fg="#333")
payment_entry.pack(pady=10, padx=20)
payment_entry.insert(0, "Digite o valor pago")
payment_entry.bind("<FocusIn>", lambda e: payment_entry.delete(0, tk.END))
payment_entry.bind("<KeyRelease>", lambda e: calculate_change())

# Exibição do troco
change_frame = tk.Frame(main_frame, bg="#f4f4f4")
change_frame.pack(pady=20)

change_label_text = tk.Label(change_frame, text="Troco: ", font=("Arial", 14), bg="#f4f4f4", fg="#6200ea")
change_label_text.pack(side="left")

change_label = tk.Label(change_frame, text="R$0.00", font=("Arial", 14, "bold"), bg="#f4f4f4", fg="#28a745")
change_label.pack(side="left")

# Inicia o loop principal
root.mainloop()
