/*
funcion pido valor, puedo dejarla empty y q  devuelva todos o pedir uno y q devuelva ese
*/

const myRequest = new Request(
  "https://www.dolarsi.com/api/api.php?type=valoresprincipales"
);

const myURL = myRequest.url; // http://localhost/api
const myMethod = myRequest.method; // POST
const myCred = myRequest.credentials; // omit
const bodyUsed = myRequest.bodyUsed; // true

fetch(myRequest)
  .then((response) => {
    if (response.status === 200) {
      return response.json();
    } else {
      throw new Error("Something went wrong on api server!");
    }
  })
  .then((response) => {
    //console.debug(response);
    for (var casa of response) {
      console.log(
        "Tipo de cambio:" +
          casa.casa.nombre +
          "\n valor de venta: " +
          casa.casa.venta +
          "\n"
      );
    }

    // ...
  })
  .catch((error) => {
    console.error(error);
  });
