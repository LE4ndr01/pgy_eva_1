$(function() {
	// El número de botas de productos básicos aumentó
	$("#add").click(function() {
		// Obtiene el valor predeterminado 1
		var old = $("#num_1").val();
		// Cada vez que haga clic en el botón, la cantidad se agregará cada vez, por ejemplo: 2 + 1 = 3,3 + 1 = 4
		var newz = parseInt(old) + 1;
		// El valor obtenido sumando 1 cada vez se envía al cuadro
		$("#num_1").val(newz);
		// Subtotal de productos básicos, la cantidad de productos disminuye y el precio disminuye en consecuencia
		// Obtener el precio unitario del producto
		var price = $("#cost").val();
		// Obtener la cantidad de bienes
		var num = $("#num_1").val();
		// Obtén el precio del lápiz labial
		var lipstick = $("#prices").val();
		// Obtenga precios de cosméticos
		var makeup = $("#pricees").val();
		// Precio total de las botas = precio unitario * cantidad
		var sum = price * num;
		// Precio total de todos los productos
		var sums = parseInt(lipstick) + parseInt(makeup) + parseInt(sum);
		// La salida del cuadro de entrada con el precio de identificación muestra el precio final de las botas
		$("#price").val(sum);
		// La salida muestra el precio total de todos los productos básicos
		$("#total").html(sums);
		
	});
	// El número de mercancías disminuye
	$("#minus").click(function() {
		var old = $("#num_1").val();
		var newz = parseInt(old) - 1;
		// Juzgar la competencia del producto no puede ser menor a 1
		if(newz < 1) {
			alert("¡La cantidad de mercancías no puede ser inferior a 1 pieza!")
		} else {
			$("#num_1").val(newz);
		}
		// Subtotal de productos, a medida que aumenta la cantidad de productos, el precio aumenta en consecuencia
		// Obtener el precio unitario del producto
		var price = $("#cost").val();
		// Obtener la cantidad de bienes
		var num = $("#num_1").val();
		// Precio total = precio unitario * cantidad
		var sum = price * num;
		// Obtén el precio del lápiz labial
		var lipstick = $("#prices").val();
		// Obtenga precios de cosméticos
		var makeup = $("#pricees").val();
		// Precio total de todos los productos
		var sums = parseInt(lipstick) + parseInt(makeup) + parseInt(sum);
		// El precio final se muestra en la salida del cuadro de entrada con el precio de identificación
		$("#price").val(sum);
		$("#total").html(sums);
	});
	// Eliminar producto
	$('#delete').click(function() {
		$("#commodity").remove();
		// Obtén el precio del lápiz labial
		var lipstick = $("#prices").val();
		// Obtenga precios de cosméticos
		var makeup = $("#pricees").val();
		var sums = parseInt(lipstick) + parseInt(makeup);
		$("#total").html(sums);
	});

	// Ha aumentado la cantidad de lápices labiales básicos
	$("#adds").click(function() {
		var old = $("#num_1s").val();
		var newz = parseInt(old) + 1;
		$("#num_1s").val(newz);
		// Subtotal de productos básicos, la cantidad de productos disminuye y el precio disminuye en consecuencia
		// Obtener el precio unitario del producto
		var price = $("#costs").val();
		// Obtener la cantidad de bienes
		var num = $("#num_1s").val();
		// Obtén el precio de las botas
		var boot = $("#price").val();
		// Obtenga precios de cosméticos
		var makeup = $("#pricees").val();
		// Precio total = precio unitario * cantidad
		var sum = price * num;
		// Precio total de todos los productos
		var sums = parseInt(boot) + parseInt(makeup) + parseInt(sum);
		// El precio final se muestra en la salida del cuadro de entrada con el precio de identificación
		$("#prices").val(sum);
		$("#total").html(sums);
	});
	// El número de mercancías disminuye
	$("#minuss").click(function() {
		var old = $("#num_1s").val();
		var newz = parseInt(old) - 1;
		// Juzgar la competencia del producto no puede ser menor a 1
		if(newz < 1) {
			alert("¡La cantidad de mercancías no puede ser inferior a 1 pieza!")
		} else {
			$("#num_1s").val(newz);
		}
		// Subtotal de productos, a medida que aumenta la cantidad de productos, el precio aumenta en consecuencia
		// Obtener el precio unitario del producto
		var price = $("#costs").val();
		// Obtener la cantidad de bienes
		var num = $("#num_1s").val();
		// Obtén el precio de las botas
		var boot = $("#price").val();
		// Obtenga precios de cosméticos
		var makeup = $("#pricees").val();
		// Precio total = precio unitario * cantidad
		var sum = price * num;
		// Precio total de todos los productos
		var sums = parseInt(boot) + parseInt(makeup) + parseInt(sum);
		// El precio final se muestra en la salida del cuadro de entrada con el precio de identificación
		$("#prices").val(sum);
		$("#total").html(sums);
	});
	// Eliminar producto
	$('#deletes').click(function() {
		$("#commoditys").remove();
	});

	//// El número de cosméticos comerciales ha aumentado
	$("#addes").click(function() {
		var old = $("#num_1es").val();
		var newz = parseInt(old) + 1;
		$("#num_1es").val(newz);
		// Subtotal de productos básicos, la cantidad de productos disminuye y el precio disminuye en consecuencia
		// Obtener el precio unitario del producto
		var price = $("#costes").val();
		// Obtener la cantidad de bienes
		var num = $("#num_1es").val();
		// Precio total = precio unitario * cantidad
		var sum = price * num;
		var boot = $("#price").val();
		var lipstick = $("#prices").val();
		var sums = parseInt(sum) + parseInt(boot) + parseInt(lipstick);
		// El precio final se muestra en la salida del cuadro de entrada con el precio de identificación
		$("#pricees").val(sum);
		$("#total").html(sums);
	});
	// El número de mercancías disminuye
	$("#minuses").click(function() {
		var old = $("#num_1es").val();
		var newz = parseInt(old) - 1;
		// Juzgar la competencia del producto no puede ser menor a 1
		if(newz < 1) {
			alert("¡La cantidad de mercancías no puede ser inferior a 1 pieza!")
		} else {
			$("#num_1es").val(newz);
		}
		// Subtotal de productos, a medida que aumenta la cantidad de productos, el precio aumenta en consecuencia
		// Obtener el precio unitario del producto
		var price = $("#costes").val();
		// Obtener la cantidad de bienes
		var num = $("#num_1es").val();
		// Precio total = precio unitario * cantidad
		var sum = price * num;
		var boot = $("#price").val();
		var lipstick = $("#prices").val();
		var sums = parseInt(sum) + parseInt(boot) + parseInt(lipstick);
		// El precio final se muestra en la salida del cuadro de entrada con el precio de identificación
		$("#pricees").val(sum);
		$("#total").html(sums);
	});
	// Eliminar producto
	$('#deletees').click(function() {
		$("#commodityes").remove();
	});

	// Botón Seleccionar todo
	$("#all").click(function() {
		var oInput = document.getElementsByName("product");
		for(var i = 0; i < oInput.length; i++) {
			oInput[i].checked = document.getElementById("all").checked;
		}
		// Obtén el precio de tres artículos
		var boot = $("#price").val();
		var lipstick = $("#prices").val();
		var makeup = $("#pricees").val();
		// Precio de liquidación = la suma de los precios de tres artículos
		var sum = parseInt(boot) + parseInt(lipstick) + parseInt(makeup);
		// Muestra el precio total en el cuadro de entrada del total de bits de identificación
		$("#total").html(sum);
		// Haga clic en el botón eliminar para eliminar el elemento
		$("#deleteAll").click(function(){
			$("#commodity,#commoditys,#commodityes").remove();
			var sum = 0;
			$("#total").html(sum);
		});
	});
});
