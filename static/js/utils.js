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

function showMsg(msg) {
	$('.modal-body').text(msg);
	$('#staticBackdrop').modal();
}
