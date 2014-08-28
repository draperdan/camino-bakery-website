		// Find the instance of a.m. or p.m. causing a double period at the end of a sentence, then kill the extra period
			$("#special_today").text(function(index, text) {
				return text.replace("..", ".");
			});