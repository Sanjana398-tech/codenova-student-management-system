"use strict";

document.addEventListener("DOMContentLoaded", () => {
    let gpaChart = null;

    // ------------------------------
    // DARK MODE
    // ------------------------------

    const themeToggle = document.getElementById("theme-toggle");

    function applyTheme(theme) {
        const isDark = theme === "dark";

        document.body.classList.toggle("dark-mode", isDark);

        themeToggle.textContent = isDark ? "☀️" : "🌙";

        themeToggle.setAttribute(
            "aria-label",
            isDark ? "Switch to light mode" : "Switch to dark mode"
        );

        themeToggle.title = isDark ? "Light mode" : "Dark mode";

        if (gpaChart) {
            updateChartTheme(gpaChart);
        }
    }

    let savedTheme = "light";

    try {
        savedTheme =
            localStorage.getItem("student-dashboard-theme") || "light";
    } catch (error) {
        console.warn("Theme preference could not be loaded.");
    }

    applyTheme(savedTheme);

    themeToggle.addEventListener("click", () => {
        const newTheme = document.body.classList.contains("dark-mode")
            ? "light"
            : "dark";

        try {
            localStorage.setItem("student-dashboard-theme", newTheme);
        } catch (error) {
            console.warn("Theme preference could not be saved.");
        }

        applyTheme(newTheme);
    });


    // ------------------------------
    // MOBILE NAVIGATION
    // ------------------------------

    const menuToggle = document.getElementById("menu-toggle");
    const sidebar = document.getElementById("sidebar");

    if (menuToggle && sidebar) {
        menuToggle.addEventListener("click", () => {
            sidebar.classList.toggle("mobile-open");

            menuToggle.textContent = sidebar.classList.contains("mobile-open")
                ? "✕ Close Menu"
                : "☰ Menu";
        });

        sidebar.querySelectorAll(".nav-item").forEach((item) => {
            item.addEventListener("click", () => {
                sidebar.classList.remove("mobile-open");
                menuToggle.textContent = "☰ Menu";
            });
        });

        document.addEventListener("click", (event) => {
            if (
                window.innerWidth <= 760 &&
                sidebar.classList.contains("mobile-open") &&
                !sidebar.contains(event.target) &&
                !menuToggle.contains(event.target)
            ) {
                sidebar.classList.remove("mobile-open");
                menuToggle.textContent = "☰ Menu";
            }
        });
    }


    // ------------------------------
    // FLASH NOTIFICATIONS
    // ------------------------------

    document.querySelectorAll(".flash").forEach((message) => {
        const closeButton = message.querySelector(".flash-close");

        function dismissMessage() {
            message.style.transition =
                "opacity 0.4s ease, transform 0.4s ease";

            message.style.opacity = "0";
            message.style.transform = "translateY(-8px)";

            setTimeout(() => message.remove(), 400);
        }

        if (closeButton) {
            closeButton.addEventListener("click", dismissMessage);
        }

        setTimeout(dismissMessage, 4500);
    });


    // ------------------------------
    // DELETE CONFIRMATION MODAL
    // ------------------------------

    const deleteModal = document.getElementById("delete-modal");
    const modalMessage = document.getElementById("modal-message");
    const cancelDelete = document.getElementById("cancel-delete");
    const confirmDelete = document.getElementById("confirm-delete");

    let selectedDeleteForm = null;

    document.querySelectorAll(".delete-form").forEach((form) => {
        form.addEventListener("submit", (event) => {
            event.preventDefault();

            selectedDeleteForm = form;

            const studentName =
                form.dataset.studentName || "this student";

            modalMessage.textContent =
                `Are you sure you want to delete ${studentName}? ` +
                "This action cannot be undone.";

            deleteModal.hidden = false;

            cancelDelete.focus();
        });
    });

    function closeDeleteModal() {
        deleteModal.hidden = true;
        selectedDeleteForm = null;
    }

    cancelDelete.addEventListener("click", closeDeleteModal);

    deleteModal.addEventListener("click", (event) => {
        if (event.target === deleteModal) {
            closeDeleteModal();
        }
    });

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape" && !deleteModal.hidden) {
            closeDeleteModal();
        }
    });

    confirmDelete.addEventListener("click", () => {
        if (selectedDeleteForm) {
            selectedDeleteForm.submit();
        }
    });


    // ------------------------------
    // LOADING FEEDBACK
    // ------------------------------

    const loadingOverlay = document.getElementById("loading-overlay");

    document.querySelectorAll(".student-form").forEach((form) => {
        form.addEventListener("submit", (event) => {
            if (!form.checkValidity()) {
                event.preventDefault();
                form.reportValidity();
                return;
            }

            loadingOverlay.hidden = false;
        });
    });

    document.querySelectorAll(".search-form").forEach((form) => {
        form.addEventListener("submit", () => {
            loadingOverlay.hidden = false;
        });
    });

    confirmDelete.addEventListener("click", () => {
        if (selectedDeleteForm) {
            loadingOverlay.hidden = false;
        }
    });


    // ------------------------------
    // GPA CHART
    // ------------------------------

    const chartCanvas = document.getElementById("gpaChart");
    const chartEmpty = document.getElementById("chart-empty");
    const chartInsight = document.getElementById("chart-insight");

    if (chartCanvas) {
        const labels = JSON.parse(chartCanvas.dataset.labels || "[]");
        const values = JSON.parse(chartCanvas.dataset.values || "[]");

        if (labels.length === 0 || values.length === 0) {
            chartEmpty.hidden = false;
            chartCanvas.style.display = "none";
        } else if (typeof Chart === "undefined") {
            chartEmpty.textContent =
                "GPA analytics could not load. Check your internet connection and refresh.";
            chartEmpty.hidden = false;
            chartCanvas.style.display = "none";
        } else {
            const isDark = document.body.classList.contains("dark-mode");
            const highestRangeIndex = values.indexOf(Math.max(...values));
            const rangeCount = values[highestRangeIndex];
            const highestRanges = labels.filter(
                (_, index) => values[index] === rangeCount
            );

            chartInsight.textContent =
                `Most represented ${highestRanges.length === 1 ? "range" : "ranges"}: ` +
                `${highestRanges.join(", ")} - ` +
                `${rangeCount} ${rangeCount === 1 ? "student" : "students"}`;

            const chart = new Chart(chartCanvas, {
                type: "bar",

                data: {
                    labels: labels,

                    datasets: [{
                        label: "Number of Students",
                        data: values,
                        backgroundColor: [
                            "#6478f4",
                            "#8b72ed",
                            "#36b99a",
                            "#f4ad63",
                            "#e879a0"
                        ],
                        borderRadius: 8,
                        borderSkipped: false,
                        maxBarThickness: 58
                    }]
                },

                options: {
                    responsive: true,
                    maintainAspectRatio: false,

                    animation: {
                        duration: 1000,
                        easing: "easeOutQuart"
                    },

                    plugins: {
                        legend: {
                            display: false
                        },

                        tooltip: {
                            backgroundColor: "#172554",
                            padding: 12,
                            cornerRadius: 8,
                            displayColors: false,
                            callbacks: {
                                label(context) {
                                    const count = context.parsed.y;
                                    return `${count} ${count === 1 ? "student" : "students"}`;
                                }
                            }
                        }
                    },

                    scales: {
                        x: {
                            grid: {
                                display: false
                            },

                            ticks: {
                                color: isDark ? "#cbd5e1" : "#71809a"
                            },

                            border: {
                                display: false
                            }
                        },

                        y: {
                            beginAtZero: true,

                            ticks: {
                                precision: 0,
                                color: isDark ? "#cbd5e1" : "#71809a"
                            },

                            grid: {
                                color: isDark
                                    ? "rgba(255,255,255,0.08)"
                                    : "rgba(100,116,139,0.12)"
                            },

                            border: {
                                display: false
                            }
                        }
                    }
                }
            });

            gpaChart = chart;
        }
    }


    // ------------------------------
    // FINISH LOADING FEEDBACK
    // ------------------------------

    function updateChartTheme(chart) {
        const isDark = document.body.classList.contains("dark-mode");

        chart.options.scales.x.ticks.color =
            isDark ? "#cbd5e1" : "#71809a";

        chart.options.scales.y.ticks.color =
            isDark ? "#cbd5e1" : "#71809a";

        chart.options.scales.y.grid.color = isDark
            ? "rgba(255,255,255,0.08)"
            : "rgba(100,116,139,0.12)";

        chart.update("none");
    }
});