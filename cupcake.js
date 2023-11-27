const BASE_URL = "http://127.0.0.1:5000/api";
//////////////////////////////////////////////////////////////////////
// This function will help generate the html.
//////////////////////////////////////////////////////////////////////
function createCupcake(cupcake){
    return `
    <div cupcake-id = ${cupcake.id}>
    <li>
    ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
    <button class= "delete-button">X</button>
    </li>
    <img class = "Cupcake-img"
                  src = " ${cupcake.image} "  
                  alt = " (no image provided) ">
    </div>
    `;
}
//////////////////////////////////////////////////////////////////////
// This function will append the new cupcakes on the page.
//////////////////////////////////////////////////////////////////////
async function showCupcakes(){
    const res = await axios.get(`${BASE_URL}/cupcakes`);

    for (let cupcakeData of res.data.cupcakes) {
        let newCupcake = $(createCupcake(cupcakeData));
        $("#cupcakes-list").append(newCupcake) ;
    }
}

//////////////////////////////////////////////////////////////////////
// This code will handel the form for adding new cupcakes
//////////////////////////////////////////////////////////////////////

$("#new-cupcake-form").on("submit", async function(evt){
    evy.preventDefault();

    let flavor = $("#form-flavor").val();
    let rating = $("#form-rating").val();
    let size = $("#form-size").val();
    let image = $("#form-image").val();

    const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`,{
        flavor,
        rating,
        size,
        image
    });

    let newCupcake = $(createCupcake(newCupcakeResponse.data.cupcake));
    $("#cupcake-list").append(newCupcake);
    $("#new-cupcake-form").trigger("reset");
});

//////////////////////////////////////////////////////////////////////
// This code will help handel deleting cupcakes
//////////////////////////////////////////////////////////////////////

$("#cupcakes-list").on("click",".delete-button", async function (evt){
    evt.preventDefault();
    let $cupcake = $(evt.target).closest("div");
    let cupcakeId = $cupcake.attr("data-cupcake-id");

    await axios.delete(`${BASE_URL} / cupcakes/ ${cupcakeId}`);
    $cupcake.remove();
});

$(showInitialcupcakes);