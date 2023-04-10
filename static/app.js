async function submitForm(event) {
    event.preventDefault();
  
    const possibility = document.getElementById("possibility").value;
    if (!possibility) {
      return;
    }
  
    const response = await fetch("/parse", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ possibility: possibility }),
    });
  
    const data = await response.json();
  
    updateSlot("goal-slot", data.goal);
    updateSlot("domain-slot", data.domain);
    updateSlot("conditions-slot", data.conditions.join(", "));
  }
  
  function updateSlot(slotId, content) {
    const slot = document.getElementById(slotId);
    slot.innerHTML = `<p>${content}</p>`;
    slot.classList.add("slot-animation");
  
    setTimeout(() => {
      slot.classList.remove("slot-animation");
    }, 2000);
  }
  
  document.getElementById("possibility-form").addEventListener("submit", submitForm);
  