from pyscript import document 

grade7 = {"Enrique Marquez", "Luis Tan", "Lliana Garcia", "Zia Sio"}

grade8 = {"Cassey Mallari", "Riona Narciso", "Sofia Enriquez", "Kensha Sibug"}

grade9 = {"Lucas Gonzales", "Zyren Naguit", "Pauline Chu Tan", "Ryle Gutierrez"}

grade10 = {"Megan Tan", "Lacey Aguilar", "Ishabel Manaloto", "Inigo Ducut"}

new_members = set()

def add_member(event):
    first = document.getElementById("first_name").value.strip().title()
    last = document.getElementById("last_name").value.strip().title()
    full_name = first + " " + last
    new_members.add(full_name)
    
    all_members = grade7 | grade8 | grade9 | grade10 | new_members
    member_list = "<br>".join(sorted(all_members))
    total = len(all_members)
    
    document.getElementById("output").innerHTML = f"""
        All members: <br>
        {member_list}
        <br><br>
        Total members: {total}
    """
    
    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""
