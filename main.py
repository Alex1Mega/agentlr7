
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

# Object-Attribute-Value (OAV)
oav_data = [
    ("Aircraft_101", "flight_number", "PS101"),
    ("Aircraft_101", "aircraft_type", "Passenger"),
    ("Aircraft_101", "altitude", "1500 m"),
    ("Aircraft_101", "speed", "250 km/h"),
    ("Aircraft_101", "status", "Approaching"),
    ("Controller_1", "name", "Ivan Petrenko"),
    ("Controller_1", "role", "Air Traffic Controller"),
    ("Airport_1", "name", "Boryspil"),
    ("Airport_1", "status", "Operational"),
    ("Runway_1", "runway_number", "18"),
    ("Runway_1", "status", "Available"),
    ("Landing_1", "action", "Landing"),
    ("Landing_1", "permission", "Granted"),
]

print("OBJECT-ATTRIBUTE-VALUE (OAV) REPRESENTATION")

for obj, attribute, value in oav_data:
    print(f"({obj}, {attribute}, {value})")


frames = {
    "Aircraft": {
        "flight_number": "PS101",
        "type": "Passenger aircraft",
        "altitude": "1500 m",
        "speed": "250 km/h",
        "status": "Approaching airport",
    },
    "Controller": {
        "name": "Ivan Petrenko",
        "role": "Air Traffic Controller",
        "responsibility": "Manage aircraft movement",
    },
    "Airport": {
        "name": "Boryspil",
        "status": "Operational",
        "function": "Receive and dispatch aircraft",
    },
    "Runway": {
        "number": "18",
        "status": "Available",
        "function": "Aircraft landing and takeoff",
    },
    "Landing": {
        "aircraft": "PS101",
        "controller": "Ivan Petrenko",
        "airport": "Boryspil",
        "runway": "18",
        "permission": "Granted",
        "result": "Successful landing",
    },
}

print("FRAME REPRESENTATION")
for frame_name, slots in frames.items():
    print(f"\nFrame: {frame_name}")
    for slot, value in slots.items():
        print(f"  {slot}: {value}")


# 3. Semantic network
nodes = {
    "Aircraft": (0.1, 0.65),
    "Controller": (0.5, 0.9),
    "Airport": (0.9, 0.65),
    "Runway": (0.9, 0.2),
    "Landing": (0.5, 0.4),
}

relations = [
    ("Controller", "Aircraft", "controls"),
    ("Controller", "Landing", "authorizes"),
    ("Aircraft", "Landing", "performs"),
    ("Landing", "Airport", "occurs at"),
    ("Landing", "Runway", "uses"),
    ("Airport", "Runway", "contains"),
]

print("SEMANTIC NETWORK RELATIONSHIPS")

for source, target, relation in relations:
    print(f"{source} --[{relation}]--> {target}")

# Draw the semantic network
fig, ax = plt.subplots(figsize=(11, 7))
ax.set_xlim(-0.05, 1.05)
ax.set_ylim(0.05, 1.05)
ax.axis("off")

# Draw nodes
for name, (x, y) in nodes.items():
    ax.text(
        x, y, name,
        ha="center",
        va="center",
        fontsize=11,
        bbox=dict(
            boxstyle="round,pad=0.7",
            facecolor="lightblue",
            edgecolor="black"
        ),
        zorder=3,
    )

# Draw directed relationships
for source, target, label in relations:
    x1, y1 = nodes[source]
    x2, y2 = nodes[target]

    arrow = FancyArrowPatch(
        (x1, y1),
        (x2, y2),
        arrowstyle="-|>",
        mutation_scale=15,
        shrinkA=38,
        shrinkB=38,
        connectionstyle="arc3,rad=0.08",
        color="gray",
        linewidth=1.5,
        zorder=1,
    )
    ax.add_patch(arrow)

    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2 + 0.035

    ax.text(
        mid_x,
        mid_y,
        label,
        fontsize=9,
        ha="center",
        va="center",
        bbox=dict(facecolor="white", edgecolor="none", alpha=0.85),
        zorder=2,
    )

ax.set_title("Semantic Network: Air Traffic Control System", fontsize=14, pad=20,)
plt.tight_layout()
plt.savefig("semantic_network.png", dpi=300, bbox_inches="tight")
plt.show()
print("\nSemantic network saved as semantic_network.png")
