using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Carbon.Identity.Data.Migrations.IdentityServer.ConfigurationDb
{
    /// <inheritdoc />
    public partial class dataclientSecrestupdate : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.UpdateData(
                table: "ApiScopes",
                keyColumn: "Id",
                keyValue: 1,
                column: "Created",
                value: new DateTime(2023, 3, 6, 8, 10, 7, 441, DateTimeKind.Utc).AddTicks(7000));

            migrationBuilder.UpdateData(
                table: "ClientSecrets",
                keyColumn: "Id",
                keyValue: 1,
                columns: new[] { "Created", "Value" },
                values: new object[] { new DateTime(2023, 3, 6, 8, 10, 7, 441, DateTimeKind.Utc).AddTicks(7580), "carbon@2023" });
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.UpdateData(
                table: "ApiScopes",
                keyColumn: "Id",
                keyValue: 1,
                column: "Created",
                value: new DateTime(2023, 3, 6, 7, 55, 47, 885, DateTimeKind.Utc).AddTicks(9460));

            migrationBuilder.UpdateData(
                table: "ClientSecrets",
                keyColumn: "Id",
                keyValue: 1,
                columns: new[] { "Created", "Value" },
                values: new object[] { new DateTime(2023, 3, 6, 7, 55, 47, 886, DateTimeKind.Utc).AddTicks(30), "Radeon1GB#" });
        }
    }
}
