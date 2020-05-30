var toStop = false;

function callAjax(method, value) {
	var params = {
		method: method,
		value: value,
	};

	$.ajax({
		type: 'POST',
		url: '/validate_field',
		data: params,
		success: function (data, textStatus, jqXHR) {
			if (!data.message) {
				showMsg(data.error);
				method = '#' + method;
				$(method).focus();
				toStop = true;
			} else toStop = false;
		},
		error: function (jqHXR, textStatus, errorThrown) {
			showMsg(jqXHR.status + ' ' + errorThrown);
			method = '#' + method;
			$(method).focus();
			toStop = true;
		},
	});
}

function CallAjextWithReturn(method, value, handleresult) {
	var params = {
		method: method,
		value: value,
	};

	$.ajax({
		type: 'POST',
		url: '/validate_field',
		data: params,
		success: function (result, textStatus, jqXHR) {
			handleresult(result);
		},
		error: function (jqHXR, textStatus, errorThrown) {
			showMsg(jqXHR.status + ' ' + errorThrown);
			method = '#' + method;
			$(method).focus();
		},
	});
}

function showMsg(msg) {
	$('.modal-body').text(msg);
	$('#staticBackdrop').modal();
}

var searchString = []; //Global variable for autocomplete field

function autoCompleteField(theField) {
	ajexAutoComplete(theField, function (result) {
		for (i in result[theField]) {
			searchString[theField][searchString[theField].length] = result[theField][i][theField];
		}
	});
}

function ajexAutoComplete(theField, handleResult) {
	$.ajax({
		type: 'POST',
		url: '/autocomplete',
		data: { field: theField },
		dataType: 'json',
		success: function (result, textStatus, jqXHR) {
			handleResult(result);
		},
		error: function (jqHXR, textStatus, errorThrown) {
			showMsg(jqHXR.status + ' 	' + errorThrown);
		},
	});
}

// function to verify float
function isFloat(evt) {
	var charCode = event.which ? event.which : event.keyCode;
	if (charCode != 46 && charCode > 31 && (charCode < 48 || charCode > 57)) {
		showMsg('Please enter only a valid number');
		return false;
	} else {
		//if dot sign entered more than once then don't allow to enter dot sign again. 46 is the code for dot sign
		var parts = evt.srcElement.value.split('.');
		if (parts.length > 1 && charCode == 46) {
			return false;
		}
		return true;
	}
}

//function to verify numbers
function isNumb(theField) {
	let numbers = /^[0-9]+$/;
	if (!theField.match(numbers)) return false;
	else return true;
}
