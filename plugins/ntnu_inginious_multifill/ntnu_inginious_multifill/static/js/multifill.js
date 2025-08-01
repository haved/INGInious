
"use strict";

/*
var debug_cm = null;
CodeMirror.defineInitHook( (cm) => {

  if (!cm.getTextArea || !cm.getTextArea().classList.contains('fill-in')) {
    return
  }
  debug_cm = cm;

  var editableRanges = new Array();
  var frozenRanges = new Array();
  var texts = cm.getValue().split(/{%([^]+?)%}/);
  cm.setValue("")

  function getLastPos(cm) {
    var line = CodeMirror.Pos(cm.lastLine()).line;
    return {
      line: line,
      ch: cm.getLine(line).length
    }
  }


  var oldMark;
  texts.forEach((s, i) => {
    var from = getLastPos(cm);
    cm.replaceRange(s, CodeMirror.Pos(cm.lastLine()));
    var to = getLastPos(cm);

    if (i % 2 == 0) {
      // mark range frozen
      var mark = cm.markText(from, to, {
        className: 'read-only',
        readOnly: true,
        atomic: true,
        clearWhenEmpty: false,
        inclusiveLeft: i == 0,
        inclusiveRight: i == texts.length - 1,
      })
      frozenRanges.push(mark)
      var lastRange = editableRanges[editableRanges.length - 1];
      if (lastRange && !lastRange.to) {
        lastRange.to = mark;
      }
      oldMark = mark;
    } else {
      editableRanges.push({
        from: oldMark,
        to: null,
        text: s,
        inline: from.line == to.line,
      })
    }
  })
  var inlineRanges = editableRanges.filter(r => r.inline);


  function overlaps(pos) {
    return inlineRanges.some(range => {
      var from = range.from.find().to;
      var to = range.to.find().from;
      var hasOverlap =
        pos.line == from.line &&
        pos.ch >= from.ch &&
        pos.line == to.line &&
        pos.ch <= to.ch;
      return hasOverlap;
    })
  }

  cm.on("beforeChange", (cm, change) => {
    if (change.update && overlaps(change.from)) {
      change.update(null, null, [change.text.join("")])
    }
  })

  function getRangeValue({from, to}) {
      return cm.getRange(from, to)
  }
  function getEditableRangeValue({from, to}) {
      return getRangeValue({from: from.find().to, to: to.find().from})
  }
  function getStringContent() {
    var i = 0;
    var str = "";
    while (true) {
      if (!frozenRanges[i]) {
        return str;
      }
      str += getRangeValue(frozenRanges[i].find())
      if (!editableRanges[i]) {
        return str;
      }
      str += "{%" + getEditableRangeValue(editableRanges[i]) + "%}"
      i = i + 1
    }
  }
  cm.getStringContent = getStringContent;
  cm.getValue = function () {
    return getStringContent()
  }
  cm.save = function () {
    cm.getTextArea().value = getStringContent()
  }

}
*/


/**
 * Init the editbox for a multifill problem
 * @param well: the DOM element containing the input fields
 * @param pid
 * @param problem
 */
function studio_init_template_multifill(well, pid, problem)
{
  // TODO: Remove debug output
  console.log(problem);

  jQuery.each(problem["subtasks"], function(index, elem)
  {
    studio_create_multifill_subtask(pid, elem);
  });
}

/**
 * Create the edit box for a subtask in a given multifill problem.
 * This method is used both when creating existing subtasks, and new ones
 * @param pid
 * @param subtask_data data about the subtask, empty object if new
 */
function studio_create_multifill_subtask(pid, subtask_data) {
  const well = $(studio_get_problem(pid));
  const subtask_list = $("#multifill-subtasks-" + pid, well);

  var subtask_id = 0;

  if ("id" in subtask_data)
    subtask_id = subtask_data["id"];
  else {
    // Subtasks are always created and deleted from the end
    subtask_id = subtask_list.children().length;
  }

  var row = $("#subproblem_multifill_subtask").html();
  var new_row_content = row.replace(/PID/g, pid)
                           .replace(/SUBTASK_ONE_INDEXED/g, subtask_id+1)
                           .replace(/SUBTASK/g, subtask_id);
  var new_row = $("<div></div>").html(new_row_content);
  subtask_list.append(new_row);

  var editor = registerCodeEditor($(".subproblem_multifill_text", new_row)[0], 'rst', 1);

  if("text" in subtask_data)
    editor.setValue(subtask_data["text"]);
}

/**
 * Removes the last multifill subtask, or no-op if it has none
 */
function studio_delete_multifill_last_subtask(pid) {
  const well = $(studio_get_problem(pid));
  const subtask_list = $("#multifill-subtasks-" + pid, well);

  subtask_list.children().last().remove();
}

function load_input_multifill(submissionid, key, input)
{
  /*
    if(key in input) {
        codeEditors[key].toTextArea();
        var elem = $('textarea[name="'+key+'"]')
        if (typeof input[key] === 'object'
            && 'input' in input[key]
            && 'template' in input[key]
            && input[key].template == elem.attr('data-x-template')
        ) {
            elem[0].value = input[key].input;
        } else {
            elem[0].value = elem.attr('data-x-template')
        }
        registerCodeEditor(elem[0], elem.attr('data-x-language'), elem.attr('data-x-lines'));
    } else {
        // TODO: console.log("No idea what to do here")
    }
    */
}
